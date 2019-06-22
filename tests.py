import unittest
from game import parse_input,loop_input

class InputTest(unittest.TestCase):


    def test_true_input(self):
        self.assertEqual(parse_input('5,3'), {'x': 5,'y': 3})

    def test_empty(self):
        self.assertEqual(parse_input(''), 'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')

    def test_null(self):
        self.assertEqual(parse_input(''), 'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')

    def test_string(self):
        self.assertEqual(parse_input('dsdsad'), 'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')

    def test_more_comma(self):
        self.assertEqual(parse_input('sas,sas,asa'), 'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')

    def test_numerik_and_string(self):
        self.assertEqual(parse_input('3,asasa'), 'Lütfen nümerik veri giriniz')

    def test_x_negative(self):
        self.assertEqual(parse_input('-3,5'),'İndis değeri negatif olamaz')

    def test_y_negative(self):
        self.assertEqual(parse_input('3,-5'), 'İndis değeri negatif olamaz')

    def test_x_and_y_negative(self):
        self.assertEqual(parse_input('-2,-4'), 'İndis değeri negatif olamaz')

    def test_bigger_than_max_indis(self):
        self.assertEqual(parse_input('0,10'), 'İndis değeri 7 den büyük olamaz')

    def test_bigger_than_max_indis_all(self):
        self.assertEqual(parse_input('8,10'), 'İndis değeri 7 den büyük olamaz')

    def test_loop_input_true(self):
        self.assertEqual(loop_input(2),2)

    def test_loop_input_empty(self):
        self.assertEqual(loop_input(''),'Lütfen konum girmek için 1 işlemi sonlandırmak için 2 giriniz')

    def test_loop_input_null(self):
        self.assertEqual(loop_input(None),'Lütfen konum girmek için 1 işlemi sonlandırmak için 2 giriniz')

    def test_loop_input_string(self):
        self.assertEqual(loop_input('sdas'),'Lütfen konum girmek için 1 işlemi sonlandırmak için 2 giriniz')

    def test_loop_input_other_number(self):
        self.assertEqual(loop_input('5'),'Lütfen konum girmek için 1 işlemi sonlandırmak için 2 giriniz')
