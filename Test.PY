import unittest
from FizzBuzz import *

class MonTest(unittest.TestCase):

    def setUp(self):
        print("Nouveau Test")
        self.instance=FizzBuzz()

    def test_first(self):
        self.assertTrue(expr="12Fizz")

    