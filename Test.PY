import unittest
from FizzBuzz import *

class MonTest(unittest.TestCase):

    def setUp(self):
        print("Nouveau Test")
        self.instance=FizzBuzz()

    def test_first(self):
        self.assertTrue(self.instance.affiche()[0]=="1")


    def test_last(self):
        self.assertTrue(expr="98FizzBuzz")

    def TearDown(self):
        print("fin de ce test")
    
if __name__=='__main__':
    unittest.main()