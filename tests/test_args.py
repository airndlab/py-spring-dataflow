import sys
from unittest import TestCase

from py_spring_dataflow.args import get_args, get_arg, is_enabled, get_flag


class Test(TestCase):
    def test_get_args(self):
        sys.argv = ['test.py', 'foo=bar']
        args = get_args()
        self.assertEqual(args, ['foo=bar'])

    def test_get_arg(self):
        sys.argv = ['test.py', 'foo=bar']
        arg = get_arg('foo')
        self.assertEqual(arg, 'bar')

    def test_get_arg_without_value(self):
        sys.argv = ['test.py', 'foo']
        arg = get_arg('foo')
        self.assertEqual(arg, True)

    def test_get_arg_without_arg(self):
        sys.argv = ['test.py', 'foo=bar']
        with self.assertRaises(Exception) as e:
            get_arg('bar')
        self.assertEqual(str(e.exception), 'No command line argument: bar')

    def test_get_arg_with_default(self):
        sys.argv = ['test.py', 'foo']
        arg = get_arg('test', 'foo')
        self.assertEqual(arg, 'foo')

    def test_get_flag(self):
        sys.argv = ['test.py', 'foo=true']
        flag = get_flag('foo')
        self.assertTrue(flag)

    def test_get_flag_without_value(self):
        sys.argv = ['test.py', 'foo']
        flag = get_flag('foo')
        self.assertTrue(flag)

    def test_get_flag_with_default(self):
        sys.argv = ['test.py', 'foo']
        flag = get_flag('test', 'True')
        self.assertTrue(flag)

    def test_is_enabled_without_value(self):
        enabled = is_enabled(True)
        self.assertTrue(enabled)

    def test_is_enabled_with_true(self):
        enabled = is_enabled('True')
        self.assertTrue(enabled)

    def test_is_enabled_with_false(self):
        enabled = is_enabled(False)
        self.assertFalse(enabled)

    def test_is_enabled_with_one(self):
        enabled = is_enabled('1')
        self.assertTrue(enabled)

    def test_is_enabled_with_t(self):
        enabled = is_enabled('t')
        self.assertTrue(enabled)

    def test_is_enabled_with_yes(self):
        enabled = is_enabled('Yes')
        self.assertTrue(enabled)
