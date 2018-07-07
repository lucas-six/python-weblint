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
        if isinstance(exxx, str):
            expected = {weblint.Report(exxx, path, lineno, obj)}
        else:
            assert isinstance(exxx, tuple)
            assert isinstance(lineno, tuple)
            assert isinstance(obj, tuple)

            expected = set()
            for e, l, o in zip(exxx, lineno, obj):
                expected.add(weblint.Report(e, path, l, o))
        self.assertSetEqual(weblint.htmlparser(path), expected)

    def testG00001(self):
        self._test('not_exist_file', 'G00001', 0, '')

    def test_HS0001(self):
        self._test('tests/HS0001.html', 'HS0001', 1, 'DOCTYPE')

    def test_HS0002(self):
        self._test('tests/HS0002.html', 'HS0002', 1, 'DOCTYPE')

    def test_HS0003(self):
        self._test('tests/HS0003.html', 'HS0003', 8, 'invalidtag')

    def test_HS0004(self):
        self._test('tests/HS0004.html', 'HS0004', 8, 'font')

    def test_HS0005(self):
        self._test('tests/HS0005.html', 'HS0005', 9, 'body')

    def test_HS0006(self):
        self._test('tests/HS0006.html', 'HS0006', 8, 'br')

    def test_HS0007(self):
        self._test('tests/HS0007.html', 'HS0007', 5, 'invalidattribute')

    def test_HS0008(self):
        self._test('tests/HS0008.html', 'HS0008', 7, 'bgcolor')

    def test_HS0009(self):
        self._test('tests/HS0009.html', 'HS0009', 2, 'lang 2')

    def test_HS0010(self):
        self._test('tests/HS0010.html', 'HS0010', 2, 'HTML')

    def test_HS0011(self):
        self._test('tests/HS0011.html', 'HS0011', 2, 'LANG')

    def test_HS0012(self):
        self._test('tests/HS0012.html', 'HS0012', 2, 'lang')

    def test_HS0013(self):
        exxx = ('HS0013', 'HS0018')
        lineno = (2, 0)
        obj = ('head', 'meta charset')
        self._test('tests/HS0013.html', exxx, lineno, obj)

    def test_HS0014(self):
        self._test('tests/HS0014.html', 'HS0014', 2, 'body')

    def test_HS0015(self):
        self._test('tests/HS0015.html', 'HS0015', 3, 'title')

    # def test_E01013(self):
    #     path = pathlib.Path('tests/E01013.html')
    #     expected = {
    #         weblint.Report('E01013', path, 5, 'title'),
    #         weblint.Report('E01013', path, 8, 'p')}
    #     self.assertSetEqual(weblint.htmlparser(path), expected)
