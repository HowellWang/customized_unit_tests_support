import unittest

from dict_compare.dict_compare import *


class DictCompareTestCase(unittest.TestCase):
    def test_basic(self):
        d1 = dict(a='foo')
        d2 = dict(a='foo')
        self.assertTrue(is_same_dict(d1, d2))
        self.assertFalse(is_same_dict(d1, dict(a='bar')))

    def test_dict_with_list_value(self):
        d1 = dict(a=[1, 2])
        d2 = dict(a=[2, 1])
        try:
            self.assertEqual(d1, d2)
        except AssertionError:
            self.assertTrue(is_same_dict(d1, d2))

    def test_complexity(self):
        d1 = dict(a='foo', b=1, c=[1, 2, 3])
        self.assertFalse(is_same_dict(d1, dict()))

    def test_deep_dict(self):
        d1 = dict(a=dict(b=dict(c="c1", d="d1")))
        self.assertFalse(is_same_dict(d1, dict(a=dict(b=dict(c="c1")))))

    def test_list_value_mixed_with_different_type(self):
        d1 = dict(a=['andy', 'john', dict(rel='brothers')])
        d2 = dict(a=['john', 'andy', dict(rel='brothers')])
        self.assertFalse(is_same_dict(d1, d2))

    def test_different_lengths(self):
        d1 = dict(a=["a", "b", dict(c='foo')])
        d2 = dict(a=["a", "b"])
        self.assertFalse(is_same_dict(d1, d2))


if __name__ == '__main__':
    unittest.main()
