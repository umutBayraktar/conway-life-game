
class Cell():

    #başlangıç değerlerini init içinde tanımla
    x = 0
    y = 0
    prev_status = False
    current_status = False

    def update_status(self):
        pass

    def print_status(self):
        if self.current_status:
            return '[X]'
        else :
            return '[ ]'

    def set_status(self,neighbour_count):
        if neighbour_count < 2 or neighbour_count > 3:
            self.dead()
        elif neighbour_count is 3 and self.prev_status is False:
            self.revive()
        return self.current_status


    def is_live(self):
        pass

    def is_dead(self):
        pass

    def dead(self):
        self.current_status = False
        return self.current_status

    def revive(self):
        self.current_status = True
        return self.current_status
