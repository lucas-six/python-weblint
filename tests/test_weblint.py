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

    def test_HS0016(self):
        self._test('tests/HS0016.html', 'HS0016', 5, 'title')

    def test_HS0017(self):
        self._test('tests/HS0017.html', 'HS0017', 8, 'p')

    def test_HS0018(self):
        self._test('tests/HS0018.html', 'HS0018', 0, 'meta charset')

    def test_HS0019(self):
        self._test('tests/HS0019.html', 'HS0019', 8, 'li')

    def test_HS0020(self):
        self._test('tests/HS0020.html', 'HS0020', 8, 'li')

    def test_HS0021(self):
        self._test('tests/HS0021.html', 'HS0021', 8, 'option')

    def test_HS0022(self):
        self._test('tests/HS0022.html', 'HS0022', 8, 'dt')

    def test_HS0023(self):
        self._test('tests/HS0023.html', 'HS0023', 8, 'dd')

    def test_HS0024(self):
        self._test('tests/HS0024.html', 'HS0024', 8, 'source')

    def test_HS0025(self):
        e = ('HS0025', 'HS0025')
        l = (9, 9)
        o = ('src', 'type')
        self._test('tests/HS0025.html', e, l, o)

    def test_HS0026(self):
        self._test('tests/HS0026.html', 'HS0026', 8, 'source')

    def test_HS0027(self):
        self._test('tests/HS0027.html', 'HS0027', 8, 'controls')

    def test_HS0028(self):
        self._test('tests/HS0028.html', 'HS0028', 8, 'controls')

    def test_HS0029(self):
        self._test('tests/HS0029.html', 'HS0029', 8, 'summary')

    def test_HS0030(self):
        self._test('tests/HS0030.html', 'HS0030', 9, 'summary')

    def test_HS0031(self):
        self._test('tests/HS0031.html', 'HS0031', 8, 'href')

    def test_HS0032(self):
        self._test('tests/HS0032.html', 'HS0032', 8, 'a')

    def test_HS0033(self):
        self._test('tests/HS0033.html', 'HS0033', 8, 'src')

    def test_HS0034(self):
        self._test('tests/HS0034.html', 'HS0034', 4, 'charset')

    def test_HS0035(self):
        self._test('tests/HS0035.html', 'HS0035', 8, 'type')

    def test_HS0036(self):
        e = ('HS0036',) * 6
        l = tuple(range(8, 14))
        o = ('h1', 'h2', 'h3', 'h4', 'h5', 'h6')
        self._test('tests/HS0036.html', e, l, o)

    def test_HS0037(self):
        self._test('tests/HS0037.html', 'HS0037', 9, 'id="id1"')

    def test_HS0038(self):
        e = ('HS0038',) * 2
        l = (8 ,9)
        o = ('main',) * 2
        self._test('tests/HS0038.html', e, l, o)

    def test_HS0039(self):
        self._test('tests/HS0039.html', 'HS0039', 8, 'src')

    def test_HS0040(self):
        e = ('HS0040',) * 2
        l = (6,) * 2
        o = ('rel', 'href')
        self._test('tests/HS0040.html', e, l, o)

    def test_HS0041(self):
        self._test('tests/HS0041.html', 'HS0041', 6, 'type')

    def test_HS0042(self):
        self._test('tests/HS0042.html', 'HS0042', 6, 'src')

    def test_HA0001(self):
        self._test('tests/HA0001.html', 'HA0001', 8, 'alt')

    def test_HA0002(self):
        self._test('tests/HA0002.html', 'HA0002', 8, 'video')

    def test_HA0003(self):
        self._test('tests/HA0003.html', 'HA0003', 8, 'audio')

    def test_HA0004(self):
        self._test('tests/HA0004.html', 'HA0004', 9, 'h1')

    def test_HA0005(self):
        self._test('tests/HA0005.html', 'HA0005', 8, 'alt')

    def test_HA0006(self):
        self._test('tests/HA0006.html', 'HA0006', 8, 'main')

    def test_E(self):
        e = ('HS0007', 'HS0012', 'HS0009', 'HS0009', 'HS0006', 'HS0004',
                'HS0005')
        l = (2, 2, 4, 5, 4, 9, 10)
        o = ('lang2', 'lang', 'meta charset 2', 'meta charset 2',
                'meta', 'font', 'body')
        self._test('tests/E.html', e, l, o)
