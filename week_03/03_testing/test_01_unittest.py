import unittest
import cn_01_unittest

class Test_01_unittest(unittest.TestCase):

    def test_if_it_returns_an_integer_when_inputting_integers(self):
        self.assertIsInstance(cn_01_unittest.showing_off(1,2),int)

    def test_if_it_returns_a_float_when_inputting_floats(self):
        self.assertIsInstance(cn_01_unittest.showing_off(1.5, 1.2),float)

    def test_if_it_does_not_return_a_string_when_inputting_stings(self):
        self.assertNotIsInstance(cn_01_unittest.showing_off("a","b"),str)
