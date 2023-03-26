import sys
from unittest import TestCase

from py_spring_dataflow.params import get_params, get_param, get_flag


class Test(TestCase):
    def test_get_params(self):
        sys.argv = ['test.py', '--mode=test', 'foo=bar']
        params = get_params()
        self.assertEqual(params, ['--mode=test'])

    def test_get_param(self):
        sys.argv = ['test.py', '--mode=test', 'foo=bar']
        param = get_param('mode')
        self.assertEqual(param, 'test')

    def test_get_param_without_param(self):
        sys.argv = ['test.py', '--mode=test', 'foo=bar']
        with self.assertRaises(Exception) as e:
            get_param('test')
        self.assertEqual(str(e.exception), 'No command line argument: --test')

    def test_get_flag(self):
        sys.argv = ['test.py', '--mode', 'foo=bar']
        flag = get_flag('mode')
        self.assertTrue(flag)

    def test_get_flag_as_disabled(self):
        sys.argv = ['test.py', '--mode=false', 'foo=bar']
        flag = get_flag('mode')
        self.assertFalse(flag)

    def test_get_flag_without_flag(self):
        sys.argv = ['test.py', '--mode=test', 'foo=bar']
        with self.assertRaises(Exception) as e:
            get_flag('test')
        self.assertEqual(str(e.exception), 'No command line argument: --test')
