import unittest
from game import parseInput

class InputTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(parseInput(''),'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')
