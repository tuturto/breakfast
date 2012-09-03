#   Copyright 2012 Tuukka Turto
#
#   This file is part of breakfast, a behave demo.
#
#   breakfast is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   breakfast is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with breakfast.  If not, see <http://www.gnu.org/licenses/>.

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