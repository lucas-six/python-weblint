#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018 L <leven.cn@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

'''WebLint - The Web Code Quality Tool, including both front-end (HTML, CSS,
JavaScript) and back-end (Python/Django).
'''

import argparse
import pathlib
from collections import namedtuple
from itertools import chain
from html.parser import HTMLParser

from requests_html import HTML


Report = namedtuple('Report', ['rule', 'path', 'lineno', 'object'])


def htmlparser(path: pathlib.Path, doctype: str ='DOCTYPE html'):
    '''HTML Parser.'''

    DEPRECATED_TAGS = (
        'font', 'center', 's', 'strike', 'b', 'i', 'tt', 'small', 'frame',
        'acronym', 'big', 'u', 'isindex', 'basefont', 'dir', 'applet',
        'style',
    )

    REQUIRED_TAGS = {
        'html': (
            ('head', '=', 1),
            ('body', '=', 1),
        ),
        'head': (
            ('title', '=', 1),
        ),
    }

    SELFCLOSED_TAGS = ('meta', 'img', 'br', 'hr', 'input')

    CLOSE_TAGS = (
        'html', 'head', 'title', 'body', 'h1', 'h2', 'h3', 'p', 'a',
        'section', 'header', 'footer', 'aside', 'strong', 'em', 'main',
    )

    DEPRECATED_ATTRS = (
        'style', 'manifest', 'xmlns', 'align', 'alink', 'link', 'vlink',
        'text', 'background', 'bgcolor', 'border', 'char', 'charoff',
        'compact', 'frame', 'frameborder', 'hspace', 'nowrap', 'rules',
        'value', 'valign', 'accept', 'vspace',
    )

    GLOBAL_ATTRS = (
        'lang', 'id', 'class',
    )

    REQUIRED_ATTRS = {
        'html': ('lang',),
    }

    NOEMPTY_TAGS = (
        'title',
    )

    class _StdHTMLParser(HTMLParser):
        def handle_decl(self, data):
            self.doctype = data
            self.not_paired_tags = []
            self._start_tags = []
            self.duplicated_attrs = []
            self.tag_not_lowercase = []

        def handle_starttag(self, tag, attrs):

            # tag name must be in lowercase
            # Python standard module "html.parser" covert tag name from uppercase
            # to lowercase already.
            rawtag = self._raw_tag()
            if not rawtag.islower():
                self.tag_not_lowercase.append((rawtag, self.lineno))

            if tag not in SELFCLOSED_TAGS:
                self._start_tags.append(tag)
            self._handle_attrs(attrs)

        def handle_endtag(self, tag):
            if tag == self._start_tags[-1]:
                self._start_tags.pop()
            else:
                if tag not in self._start_tags:
                    self.not_paired_tags.append((tag, self.lineno))
                else:
                    for t in reversed(self._start_tags):
                        if t != tag:
                            self.not_paired_tags.append((t, self.lineno))
                        else:
                            self._start_tags.pop()
                            break

        def handle_startendtag(self, tag, attrs):
            # tag name must be in lowercase
            rawtag = self._raw_tag()
            if not rawtag.islower():
                self.tag_not_lowercase.append((rawtag, self.lineno))

            if tag not in SELFCLOSED_TAGS:
                self.not_paired_tags.append((tag, self.lineno))
            self._handle_attrs(attrs)

        def _handle_attrs(self, attrs):
            attrnames = [a[0] for a in attrs]
            for a in attrs:
                name, _ = a

                # attribute name must be lowercase
                if not name.islower():
                    pass#self.attr_name_not_lowercase.append((attr_name, self.lineno))

                # validate duplicated attributes
                c = attrnames.count(name)
                if c > 1 and (f'{name} {c}', self.lineno) not in self.duplicated_attrs:
                    self.duplicated_attrs.append((f'{name} {c}', self.lineno))

        def _raw_tag(self):
            lineno, pos = self.getpos()
            rawline = self.rawdata.splitlines()[lineno-1]
            return rawline[pos+1:pos+1+len(self.lasttag)]

    try:
        with path.open() as f:
            doc = f.read()
    except FileNotFoundError:
        return [Report('E00001', path, 0, '')]
    reports = []

    # validate DOCTYPE, using standard HTML parser since
    # requests-html ignore handling the DOCTYPE
    lineno = 1
    obj = 'DOCTYPE'
    std_parser = _StdHTMLParser()
    std_parser.feed(doc)
    try:
        if std_parser.doctype != doctype:
            reports.append(Report('E01002', path, lineno, obj))
            return reports

        rules = {
            'not_paired_tags': 'E01005',
            'duplicated_attrs': 'E01010',
            'tag_not_lowercase': 'E01011',
        }
        for a, e in rules.items():
            if hasattr(std_parser, a):
                for t in getattr(std_parser, a):
                    reports.append(Report(e, path, t[1], t[0]))

    except AttributeError:
        reports.append(Report('E01001', path, lineno, obj))
        return reports
    finally:
        std_parser.close()

    parser = HTML(html=doc)
    for element in parser.find():
        lxml_element = element.element
        tag = lxml_element.tag
        lineno = lxml_element.sourceline
        if tag in DEPRECATED_TAGS:
            reports.append(Report('E01004', path, lineno, tag))
        elif tag not in CLOSE_TAGS + SELFCLOSED_TAGS:
            reports.append(Report('E01003', path, lineno, tag))
        else:
            pass
        
        # validate required elements
        rules = REQUIRED_TAGS.get(tag)
        if rules is not None:
            for r in rules:
                if eval(f'len(element.find(r[0])) !{r[1]} r[2]'):
                    reports.append(Report('E01008', path, lineno, r[0]))

        # validate required attributes
        rules = REQUIRED_ATTRS.get(tag)
        if rules is not None:
            for r in rules:
                if r not in (a.lower() for a in element.attrs):
                    reports.append(Report('E01009', path, lineno, r))

        # parse attributes
        for a in element.attrs:
            a_lower = a
            if not a.islower():
                reports.append(Report('E01012', path, lineno, a))
                a_lower = a.lower()
            if a_lower in DEPRECATED_ATTRS:
                reports.append(Report('E01007', path, lineno, a))
            elif a_lower not in GLOBAL_ATTRS:
                reports.append(Report('E01006', path, lineno, a))

    for t in NOEMPTY_TAGS:
        for e in parser.find(t):
            if not e.text:
                reports.append(Report('E01013', path, lineno, e.element.tag))

    return reports


def main():
    parser = argparse.ArgumentParser(description='WebLint: The Web Code Quality Tool')
    parser.add_argument('source', metavar='F', type=str, nargs='+',
                    help='directory or source HTML/CSS/JavaScript file')

    reports = []
    n = 0
    for path in parser.parse_args().source:
        path = pathlib.Path(path)

        if not path.exists():
            reports.append(Report('E00001', path, 0, ''))

        elif path.is_file():
            n += 1
            reports.extend(_weblint_onefile(path))

        elif path.is_dir():
            for sub in chain(
                    path.rglob('*.html'),
                    path.rglob('*.css'),
                    path.rglob('*.js')):
                _weblint_onefile(sub)

    print(n, reports)


def _debug(msg: str):
    if __debug__:
        print(msg)


def _weblint_onefile(path: pathlib.Path) -> list:
    assert path.is_file()

    # whose suffix must be one of '.html', '.css' and '.js'
    suffix = path.suffix        
    if suffix == '.html':
        return htmlparser(path)
    elif suffix == '.css':
        raise NotImplementedError
    elif suffix == '.js':
        raise NotImplementedError

if __name__ == '__main__':
    main()
