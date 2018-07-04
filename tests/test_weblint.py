#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import pathlib

from weblint import weblint


class WebLintTests(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def _test_EXXXXX(self, fname, exxx, lineno, obj):
        path = pathlib.Path(fname)
        expected = [weblint.Report(exxx, path, lineno, obj)]
        self.assertListEqual(weblint.htmlparser(path), expected)

    def test_E00001(self):
        self._test_EXXXXX('not_exist_file', 'E00001', 0, '')

    def test_E01001(self):
        self._test_EXXXXX('tests/E01001.html', 'E01001', 1, 'DOCTYPE')

    def test_E01002(self):
        self._test_EXXXXX('tests/E01002.html', 'E01002', 1, 'DOCTYPE')

    def test_E01003(self):
        self._test_EXXXXX('tests/E01003.html', 'E01003', 7, 'invalidtag')

    def test_E01004(self):
        self._test_EXXXXX('tests/E01004.html', 'E01004', 7, 'font')

    def test_E01005(self):
        self._test_EXXXXX('tests/E01005.html', 'E01005', 8, 'body')

    def test_E01006(self):
        self._test_EXXXXX('tests/E01006.html', 'E01006', 4, 'invalidattribute')

    def test_E01007(self):
        self._test_EXXXXX('tests/E01007.html', 'E01007', 4, 'style')

    def test_E01008(self):
        self._test_EXXXXX('tests/E01008.html', 'E01008', 3, 'title')

    def test_E01009(self):
        self._test_EXXXXX('tests/E01009.html', 'E01009', 2, 'lang')

    def test_E01010(self):
        self._test_EXXXXX('tests/E01010.html', 'E01010', 2, 'lang 2')

    def test_E01011(self):
        self._test_EXXXXX('tests/E01011.html', 'E01011', 2, 'HTML')

    def test_E01012(self):
        self._test_EXXXXX('tests/E01012.html', 'E01012', 2, 'LANG')

    def test_E01013(self):
        self._test_EXXXXX('tests/E01013.html', 'E01013', 6, 'title')
