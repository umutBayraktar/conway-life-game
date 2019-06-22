import unittest
from game import parseInput

class InputTest(unittest.TestCase):


    def test_trueInput(self):
        self.assertEqual(parseInput('5,3'),{'x':5,'y':3})

    def test_empty(self):
        self.assertEqual(parseInput(''),'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')

    def test_null(self):
        self.assertEqual(parseInput(''), 'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')

    def test_string(self):
        self.assertEqual(parseInput('dsdsad'),'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')

