import unittest
from FizzBuzz import *

class MonTest(unittest.TestCase):

    def setUp(self):
        print("Nouveau Test")
        self.instance=FizzBuzz()


    def test_affiche(self):
        '''test du changement des multiples'''
        with self.subTest(self):
            self.assertTrue(self.instance.affiche(1),101)