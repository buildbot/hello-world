"""sample test"""
import unittest

from hello import hello, goodbye


class TestHello(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual(hello("world"), "hello world")

    def test_bye(self):
        self.assertEqual(goodbye("world"), "bye bye world")

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(hello("world"), "hello world")
