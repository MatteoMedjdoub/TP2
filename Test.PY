import unittest
from FizzBuzz import *

class MonTest(unittest.TestCase):

    def setUp(self):
        print("Nouveau Test")
        self.instance=FizzBuzz("premiere_class")
        

