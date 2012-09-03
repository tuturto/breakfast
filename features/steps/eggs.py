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

