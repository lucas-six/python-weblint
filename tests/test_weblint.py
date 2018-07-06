#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import pathlib

from weblint import weblint


class WebLintTests(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def _test(self, fname, exxx, lineno, obj):
        path = pathlib.Path(fname)
        expected = {weblint.Report(exxx, path, lineno, obj)}
        self.assertSetEqual(weblint.htmlparser(path), expected)

    def testG00001(self):
        self._test('not_exist_file', 'G00001', 0, '')

    def test_HS0001(self):
        self._test('tests/HS0001.html', 'HS0001', 1, 'DOCTYPE')

    def test_HS0002(self):
        self._test('tests/HS0002.html', 'HS0002', 1, 'DOCTYPE')

    def test_E01003(self):
        self._test('tests/E01003.html', 'E01003', 7, 'invalidtag')

    def test_E01004(self):
        self._test('tests/E01004.html', 'E01004', 7, 'font')

    def test_E01005(self):
        self._test('tests/E01005.html', 'E01005', 8, 'body')

    def test_E01006(self):
        self._test('tests/E01006.html', 'E01006', 4, 'invalidattribute')

    def test_E01007(self):
        self._test('tests/E01007.html', 'E01007', 4, 'style')

    def test_E01008(self):
        self._test('tests/E01008.html', 'E01008', 3, 'title')

    def test_E01009(self):
        self._test('tests/E01009.html', 'E01009', 2, 'lang')

    def test_E01010(self):
        self._test('tests/E01010.html', 'E01010', 2, 'lang 2')

    def test_E01011(self):
        self._test('tests/E01011.html', 'E01011', 2, 'HTML')

    def test_E01012(self):
        self._test('tests/E01012.html', 'E01012', 2, 'LANG')

    def test_E01013(self):
        path = pathlib.Path('tests/E01013.html')
        expected = {
            weblint.Report('E01013', path, 5, 'title'),
            weblint.Report('E01013', path, 8, 'p')}
        self.assertSetEqual(weblint.htmlparser(path), expected)
