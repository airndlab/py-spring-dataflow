import os
from unittest import TestCase

from py_spring_dataflow.envs import get_env


class Test(TestCase):
    def test_get_env(self):
        os.environ['FOO'] = 'bar'
        env = get_env('FOO')
        self.assertEqual(env, 'bar')

    def test_get_env_without_env(self):
        os.environ['FOO'] = 'bar'
        with self.assertRaises(Exception) as e:
            get_env('BAR')
        self.assertEqual(str(e.exception), 'No environment variable: BAR')
