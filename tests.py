import unittest
from game import parseInput

class InputTest(unittest.TestCase):


    def test_true_input(self):
        self.assertEqual(parseInput('5,3'), {'x': 5,'y': 3})

    def test_empty(self):
        self.assertEqual(parseInput(''), 'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')

    def test_null(self):
        self.assertEqual(parseInput(''), 'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')

    def test_string(self):
        self.assertEqual(parseInput('dsdsad'), 'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')

    def test_more_comma(self):
        self.assertEqual(parseInput('sas,sas,asa'), 'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')

    def test_numerik_and_string(self):
        self.assertEqual(parseInput('3,asasa'), 'Lütfen nümerik veri giriniz')

    def test_x_negative(self):
        self.assertEqual(parseInput('-3,5'),'İndis değeri negatif olamaz')

    def test_y_negative(self):
        self.assertEqual(parseInput('3,-5'), 'İndis değeri negatif olamaz')

    def test_x_and_y_negative(self):
        self.assertEqual(parseInput('-2,-4'), 'İndis değeri negatif olamaz')

    def test_bigger_than_max_indis(self):
        self.assertEqual(parseInput('0,10'), 'İndis değeri 7 den büyük olamaz')
