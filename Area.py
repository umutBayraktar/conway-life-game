from Cell import Cell


class Area():

    array = range(0, 8)
    cells = [[], [], [], [], [], [], [], []]

    def __init__(self, input_array):
        for i in self.array:
            for j in self.array:
                self.cells[i].append(Cell())
        for c in input_array:
            self.cells[c['x']][c['y']].prev_status = True
            self.cells[c['x']][c['y']].revive()



    def print_area(self):
        temp = ""
        for i in self.array:
            for j in self.array:
                temp += self.cells[j][i].print_status()
            temp += "\n"
        return temp

    def check_environment(self,x,y):
        neighbor_count = 0
        if x < 0 or y < 0:
            return -1
        top = y-1
        buttom = y+1
        left = x-1
        rigth = x+1
        if top >= 0:
            top_cell = self.cells[x][top]
            if top_cell.is_live():
                neighbor_count += 1
            if left >= 0:
                top_left_cell = self.cells[left][top]
                if top_left_cell.is_live():
                    neighbor_count += 1
            if rigth <= 7:
                top_rigth_cell= self.cells[rigth][top]
                if top_rigth_cell.is_live():
                    neighbor_count +=1
        if buttom <= 7:
            buttom_cell=self.cells[x][buttom]
            if buttom_cell.is_live():
                neighbor_count += 1

            if left >= 0:
                buttom_left_cell = self.cells[left][buttom]
                if buttom_left_cell.is_live():
                    neighbor_count += 1
            if rigth <= 7:
                buttom_rigth_cell= self.cells[rigth][buttom]
                if buttom_rigth_cell.is_live():
                    neighbor_count +=1
        if left >= 0:
            left_cell= self.cells[left][y]
            if left_cell.is_live():
                neighbor_count += 1
        if rigth <= 7:
            rigth_cell=self.cells[rigth][y]
            if rigth_cell.is_live():
                neighbor_count += 1
        return neighbor_count