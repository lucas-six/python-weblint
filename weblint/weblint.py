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


def htmlparser(path: pathlib.Path, doctype: str ='DOCTYPE html') -> set:
    '''HTML Parser.'''

    DEPRECATED_TAGS = {
        'font', 'center', 's', 'strike', 'b', 'i', 'tt', 'small', 'frame',
        'acronym', 'big', 'u', 'isindex', 'basefont', 'dir', 'applet',
        'style',
    }

    REQUIRED_TAGS = {
        'html': (
            (('head', '==', 1), 'HS0013'),
            (('body', '==', 1), 'HS0014'),
        ),
        'head': (
            (('title', '==', 1), 'HS0015'),
            (('meta', '>=', 1), 'HS0018'),
        ),
        'ul': (
            (('li', '>=', 1), 'HS0019'),
        ),
        'ol': (
            (('li', '>=', 1), 'HS0020'),
        ),
        'select': (
            (('option', '>=', 1), 'HS0021'),
        ),
        'dl': (
            (('dt', '>=', 1), 'HS0022'),
            (('dd', '>=', 1), 'HS0023'),
        ),
        'video': (
            (('source', '>=', 1), 'HS0024'),
        ),
        'audio': (
            (('source', '>=', 1), 'HS0026'),
        ),
    }

    SELFCLOSED_TAGS = {
        'area', 'base', 'br', 'embed', 'hr', 'iframe', 'input', 'img', 'keygen',
        'link', 'meta', 'output', 'param', 'track', 'wbr', 'source',
    }

    CLOSE_TAGS = {
        'a', 'abbr', 'address', 'article', 'aside', 'audio',
        'bdi', 'bdo', 'blockquote', 'body', 'button',
        'canvas', 'caption', 'cite', 'code', 'col', 'colgroup',
        'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'dialog', 'div',
            'dl', 'dt',
        'em',
        'fieldset', 'figure', 'figcaption', 'footer', 'form', 'frameset',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hgroup', 'html',
        'ins',
        'kbd',
        'label', 'legend', 'li',
        'main', 'map', 'menu', 'menuitem', 'meter',
        'nav', 'noscript',
        'object', 'ol', 'option', 'optgroup',
        'p', 'picture', 'pre', 'progress',
        'q',
        'rb', 'rp', 'rt', 'rtc', 'ruby',
        'samp', 'script', 'section', 'select', 'span', 'strong',
            'sub', 'sup',
        'table', 'textarea', 'tbody', 'td', 'template', 'th', 'thead', 'time',
            'title', 'tfoot', 'tr',
        'ul',
        'var', 'video'
    }

    DEPRECATED_ATTRS = {
        'style', 'manifest', 'xmlns', 'align', 'alink', 'link', 'vlink',
        'text', 'background', 'bgcolor', 'border', 'char', 'charoff',
        'compact', 'frame', 'frameborder', 'hspace', 'nowrap', 'rules',
        'value', 'valign', 'accept', 'vspace', 'noframes'
    }

    GLOBAL_ATTRS = {
        'lang', 'id', 'class',
    }

    VALID_ATTRS = {
        'charset', 'name', 'src', 'content', 'controls', 'type',
    }

    REQUIRED_ATTRS = {
        'html': (('lang',), 'HS0012'),
        'video': (('controls',), 'HS0027'),
        'source': (('src', 'type'), 'HS0025'),
        'audio': (('controls',), 'HS0028'),
    }

    NOEMPTY_TAGS = {
        ('title', 'HS0016'),
        ('p', 'HS0017'),
    }

    class _StdHTMLParser(HTMLParser):
        def handle_decl(self, data):
            self.doctype = data
            self.not_paired_tags = []
            self._start_tags = []
            self.duplicated_attrs = []
            self.tag_not_lowercase = []
            self.empty_tags_not_closed = []

        def handle_starttag(self, tag, attrs):

            # tag name must be in lowercase
            # Python standard module "html.parser" covert tag name from uppercase
            # to lowercase already.
            rawtag = self._raw_tag()
            if not rawtag.islower():
                self.tag_not_lowercase.append((rawtag, self.lineno))

            if tag not in SELFCLOSED_TAGS:
                self._start_tags.append(tag)
            else:
                self.empty_tags_not_closed.append((tag, self.lineno))
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
        return {Report('G00001', path, 0, '')}
    reports = set()

    # validate DOCTYPE, using standard HTML parser since
    # requests-html ignore handling the DOCTYPE
    lineno = 1
    obj = 'DOCTYPE'
    std_parser = _StdHTMLParser()
    std_parser.feed(doc)
    try:
        if std_parser.doctype != doctype:
            reports.add(Report('HS0002', path, lineno, obj))
            return reports

        rules = {
            'not_paired_tags': 'HS0005',
            'empty_tags_not_closed': 'HS0006',
            'duplicated_attrs': 'HS0009',
            'tag_not_lowercase': 'HS0010',
        }
        for a, e in rules.items():
            if hasattr(std_parser, a):
                for t in getattr(std_parser, a):
                    reports.add(Report(e, path, t[1], t[0]))

    except AttributeError:
        reports.add(Report('HS0001', path, lineno, obj))
        return reports
    finally:
        std_parser.close()

    parser = HTML(html=doc)
    for element in parser.find():
        lxml_element = element.element
        tag = lxml_element.tag
        lineno = lxml_element.sourceline
        if tag in DEPRECATED_TAGS:
            reports.add(Report('HS0004', path, lineno, tag))
        elif tag not in CLOSE_TAGS | SELFCLOSED_TAGS:
            reports.add(Report('HS0003', path, lineno, tag))
        else:
            pass
        
        # validate required elements
        rules = REQUIRED_TAGS.get(tag)
        if rules is not None:
            for r in rules:
                if eval(f'not len(element.find(r[0][0])) {r[0][1]} r[0][2]'):
                    reports.add(Report(r[1], path, lineno, r[0][0]))

        # validate required attributes
        rules = REQUIRED_ATTRS.get(tag)
        if rules is not None:
            for r in rules[0]:
                if r not in (a.lower() for a in element.attrs):
                    reports.add(Report(rules[1], path, lineno, r))

        # parse attributes
        for a in element.attrs:
            a_lower = a

            # validate attribute name must be in lowercase
            if not a.islower():
                reports.add(Report('HS0011', path, lineno, a))
                a_lower = a.lower()

            if a_lower in DEPRECATED_ATTRS:
                reports.add(Report('HS0008', path, lineno, a))
            elif a_lower not in GLOBAL_ATTRS | VALID_ATTRS:
                reports.add(Report('HS0007', path, lineno, a))                

    for t in NOEMPTY_TAGS:
        for e in parser.find(t[0]):
            if not e.text:
                reports.add(Report(t[1], path, e.element.sourceline, e.element.tag))

    # <meta charset=""> element required one time
    found = 0
    for e in parser.find('meta'):
        if 'charset' in e.attrs:
            found += 1
    if not found:
        reports.add(Report('HS0018', path, 0, 'meta charset'))
    elif found > 1:
        reports.add(Report('HS0009', path, 0, f'meta charset {found}'))

    return reports


def main():
    parser = argparse.ArgumentParser(description='WebLint: The Web Code Quality Tool')
    parser.add_argument('source', metavar='F', type=str, nargs='+',
                    help='directory or source HTML/CSS/JavaScript file')

    reports = set()
    n = 0
    for path in parser.parse_args().source:
        path = pathlib.Path(path)

        if not path.exists():
            reports.add(Report('G00001', path, 0, ''))

        elif path.is_file():
            n += 1
            reports |= _weblint_onefile(path)

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


def _weblint_onefile(path: pathlib.Path) -> set:
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
