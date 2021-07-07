import unittest

import stactools.ga_nlcd


class TestModule(unittest.TestCase):
    def test_version(self):
        self.assertIsNotNone(stactools.ga_nlcd.__version__)
