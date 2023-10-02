import unittest
from FizzBuzz import *

class MonTest(unittest.TestCase):

    def setUp(self):
        print("Nouveau Test")
        self.instance=FizzBuzz()

    def test_first(self):
        self.assertTrue(expr="12Fizz")


    def test_last(self):
        self.assertTrue(expr="98FizzBuzz")

    def TearDown(self):
        print("fin de ce test")
    
    if name=='main':
        unittest.main()