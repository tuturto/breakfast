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

from breakfast import BreakfastMachine
from ui import BreakfastUI
from mockito import verify, mock
from behave import *

@given(u'machine is standing by')
def impl(context):
    context.ui = mock(BreakfastUI)
    context.machine = BreakfastMachine(context.ui)

@given(u'machine has {egg_amount} eggs')
def impl(context, egg_amount):
    context.machine.eggs = int(egg_amount)

@given(u'egg setting is {egg_hardness}')
def impl(context, egg_hardness):
    context.machine.egg_hardness = egg_hardness

@given(u'amount of eggs to boil is set to {amount}')
def impl(context, amount):
    context.machine.eggs_to_boil = int(amount)

@when(u'machine boils eggs')
def impl(context):
    context.machine.boil_eggs()

@then(u'there should be {amount} boiled egg')
def impl(context, amount):
    assert context.machine.boiled_eggs == int(amount)

@then(u'eggs should be {hardness}')
def impl(context, hardness):
    assert context.machine.boiled_egg_hardness == hardness

@then(u'there should be error message "{message}"')
def impl(context, message):
    verify(context.machine.ui).error(message)

