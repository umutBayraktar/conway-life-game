
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
