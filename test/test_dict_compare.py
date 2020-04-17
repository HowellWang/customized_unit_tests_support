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
        self.assertTrue(is_same_dict(d1, d2))

    def test_dict_with_complicated_list_value(self):
        d1 = dict(a=dict(b=[1, 2]), c=['test1', 'test2'])
        d2 = dict(a=dict(b=[2, 1]), c=['test2', 'test1'])
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
        self.assertTrue(is_same_dict(d1, d2))

    def test_dict_with_different_lengths(self):
        d1 = dict(a=["a", "b", dict(c='foo')])
        d2 = dict(a=["a", "b"])
        self.assertFalse(is_same_dict(d1, d2))


class TestListCompareTestCase(unittest.TestCase):
    def test_basic_list(self):
        self.assertTrue(is_same_list([1, 2], [1, 2]))
        self.assertTrue(is_same_list([1, 2], [2, 1]))

    def test_list_with_dict(self):
        l1 = ['andy', 'john', dict(rel='brothers')]
        l2 = ['john', 'andy', dict(rel='brothers')]
        self.assertTrue(is_same_list(l1, l2))
