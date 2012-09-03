class BreakfastMachine(object):
    def __init__(self, ui):
        super(BreakfastMachine, self).__init__()
        self.ui = ui
        self.eggs = 0

        self.egg_hardness = 'soft'       
        self.eggs_to_boil = 0
        
        self.boiled_eggs = 0
        self.boiled_egg_hardness = None
        
    def boil_eggs(self):
        if self.eggs_to_boil <= self.eggs:
            self.boiled_eggs = self.eggs_to_boil
            self.boiled_egg_hardness = self.egg_hardness
            self.eggs = self.eggs - self.eggs_to_boil
        else:
            self.boiled_eggs = 0
            self.boiled_egg_hardness = None
            self.ui.error('not enough eggs')