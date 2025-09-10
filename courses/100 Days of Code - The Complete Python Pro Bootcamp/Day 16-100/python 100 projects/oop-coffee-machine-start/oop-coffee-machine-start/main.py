from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu1 = Menu()
coffee_maker1 = CoffeeMaker()
money_machine1 = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"What would you like? ({menu1.get_items()}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker1.report()
        money_machine1.report()
    order = menu1.find_drink(choice)
    if order:
        if coffee_maker1.is_resource_sufficient(order):
            if money_machine1.make_payment(order.cost):
                coffee_maker1.make_coffee(order)




