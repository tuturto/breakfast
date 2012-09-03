Feature: Boiling eggs
  as an user
  in order to have breakfast
  I want machine to boil eggs

  Background:
    Given machine is standing by

  Scenario: boil hard egg
     Given machine has 10 eggs
       And egg setting is hard
       And amount of eggs to boil is set to 1
      When machine boils eggs
      Then there should be 1 boiled egg
       And eggs should be hard
       
  Scenario: boiling too many eggs should give an error
     Given machine has 1 eggs
       And amount of eggs to boil is set to 5
      When machine boils eggs
      Then there should be error message "not enough eggs"

