import unittest
from game import parse_input,loop_input
from Cell import Cell
from Area import Area

class InputTest(unittest.TestCase):


    def test_true_input(self):
        self.assertEqual(parse_input('5,3'), {'x': 5,'y': 3})

    def test_empty(self):
        self.assertEqual(parse_input(''), None)
    def test_null(self):
        self.assertEqual(parse_input(''),None)

    def test_string(self):
        self.assertEqual(parse_input('dsdsad'), None)

    def test_more_comma(self):
        self.assertEqual(parse_input('sas,sas,asa'), None)

    def test_numerik_and_string(self):
        self.assertEqual(parse_input('3,asasa'), None)

    def test_x_negative(self):
        self.assertEqual(parse_input('-3,5'),None)

    def test_y_negative(self):
        self.assertEqual(parse_input('3,-5'), None)

    def test_x_and_y_negative(self):
        self.assertEqual(parse_input('-2,-4'), None)

    def test_bigger_than_max_indis(self):
        self.assertEqual(parse_input('0,10'), None)

    def test_bigger_than_max_indis_all(self):
        self.assertEqual(parse_input('8,10'), None)

    def test_loop_input_true(self):
        self.assertEqual(loop_input(1), 1)

    def test_loop_input_empty(self):
        self.assertEqual(loop_input(''), -1)

    def test_loop_input_null(self):
        self.assertEqual(loop_input(None), -1)

    def test_loop_input_string(self):
        self.assertEqual(loop_input('sdas'), -1)

    def test_loop_input_other_number(self):
        self.assertEqual(loop_input('5'), -1)


class CellTests(unittest.TestCase):

    def test_revive(self):
        cell_object = Cell()
        self.assertEqual(cell_object.revive(), True)

    def test_dead(self):
        cell_object=Cell()
        self.assertEqual(cell_object.dead(), False)

    def test_print_status_live(self):
        cell_object=Cell()
        cell_object.current_status = True
        self.assertEqual(cell_object.print_status(), '[X]')

    def test_print_status_dead(self):
        cell_object = Cell()
        cell_object.current_status = False
        self.assertEqual(cell_object.print_status(), '[ ]')

    def test_set_status_count_2_alive(self):
        cell_object = Cell()
        cell_object.current_status=True
        self.assertEqual(cell_object.set_status(2),True)

    def test_set_status_count_2_dead(self):
        cell_object = Cell()
        cell_object.current_status=False
        self.assertEqual(cell_object.set_status(2),False)

    def test_set_status_count_3_alive(self):
        cell_object = Cell()
        cell_object.current_status=True
        self.assertEqual(cell_object.set_status(3), True)

    def test_set_status_count_3_dead(self):
        cell_object = Cell()
        cell_object.current_status = False
        self.assertEqual(cell_object.set_status(3), True)

    def test_set_status_alone(self):
        cell_object = Cell()
        self.assertEqual(cell_object.set_status(1), False)

    def test_set_status_crowded(self):
        cell_object = Cell()
        self.assertEqual(cell_object.set_status(7), False)



class AreaTest(unittest.TestCase):

    def test_print_area(self):
        input_cells = [{'x': 0, 'y': 0}]
        area = Area(input_cells)
        self.assertEqual(area.print_area(),
                         "[X][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n")
    def test_print_area_2(self):
        input_cells = [{'x': 0, 'y': 0}, {'x': 1, 'y': 3}]
        area = Area(input_cells)
        self.assertEqual(area.print_area(),
                         "[X][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][X][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
                         "[ ][ ][ ][ ][ ][ ][ ][ ]\n")