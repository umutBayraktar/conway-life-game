from .Cell import Cell


class Area():

    array = range(0, 8)
    cells = [[], [], [], [], [], [], [], []]

    def __init__(self):
        for i in self.array:
            for j in self.array:
                self.cells[i].append(Cell())

    def set_cell_live(self,x,y):
        pass

    def print_area(self):
        pass

    def examine_environment(self):
        pass
