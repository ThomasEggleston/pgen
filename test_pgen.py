from pgen import Pgen
import unittest

class Testpgen(unittest.TestCase):
    def setUp(self):
        length = 8
        self.password = Pgen.password(tags="", length)

    def test_length(self):
        self.assertTrue(len(self.password) == 8)
