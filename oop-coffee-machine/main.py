from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

on = True
while on:
    choice = input(f"What would you like to have ? {machine.get_items()}: ")
    if choice == 'off':
        on = False
    elif choice == 'report':
        print(coffee.report())
        print(money.report())
    else:
        drink = machine.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            print(coffee.make_coffee(drink))







