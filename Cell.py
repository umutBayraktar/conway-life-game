
class Cell():

    #başlangıç değerlerini init içinde tanımla


    def __init__(self):
        self.x = 0
        self.y = 0
        self.prev_status=False
        self.current_status=False

    def update_status(self):
        pass

    def print_status(self):
        if self.current_status:
            return '[X]'
        else :
            return '[ ]'

    def set_status(self, neighbour_count):
        if neighbour_count < 2 or neighbour_count > 3:
            self.dead()
        elif neighbour_count is 3 and self.is_dead():
            self.revive()
        return self.current_status


    def is_live(self):
        return self.prev_status == True

    def is_dead(self):
        return self.prev_status == False

    def dead(self):
        self.current_status = False
        return self.current_status

    def revive(self):
        self.current_status = True
        return self.current_status

    def upgrade_status(self):
        self.prev_status=self.current_status
        return self.prev_status
