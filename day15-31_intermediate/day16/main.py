from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

off = False
while not off:
    user_choice = input(f"What would you like? {menu.get_items()}:").lower()
    if user_choice == "off":
        off = 'True'
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        chosen_coffee = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(chosen_coffee):
            coffee_cost = chosen_coffee.cost
            payment_successful = money_machine.make_payment(coffee_cost)
            if payment_successful:
                coffee_maker.make_coffee(chosen_coffee)
