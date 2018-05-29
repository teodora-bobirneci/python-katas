import unittest

from katas.hello_world import say_hello


class HelloWorldTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(say_hello(), 'Hello World!')
