MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            'milk': 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}\n')
def choose_coffee():
    """returns user_choice"""
    valid = False
    while valid == False:
        user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if user_choice == 'report':
            report()
        elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
            return user_choice
        elif user_choice  =='off':
            return user_choice
        else:
            print('that is not a valid choice')
def take_money_and_format():
    print('Please insert coins.')
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))
    #convert the above to cents
    quarters *= 25
    dimes *= 10
    nickles *= 5
    #print (f'{quarters} {dimes} {nickles} {pennies}')
    #add all the coins up together in cents and pass to output
    user_wallet = (quarters + dimes + nickles +pennies)/100
    return user_wallet
def charge_for_coffee():
    user_wallet = take_money_and_format()
    #compare the price of the coffee against total money
    price_of_coffee =(MENU['espresso']['cost'])
    if user_wallet <= price_of_coffee:
        print("Sorry that's not enough money. Money refunded.​")
        user_wallet = 0
        return 'no'
    else:
        change = user_wallet - price_of_coffee
        round(change,2)
        print(f'Here is ${change} in change.')
        resources['money'] += price_of_coffee
def check_resources(menu_item):
    """takes choice and returns rosources ok"""
    ## what does the coffee need
    #this can sureley be done better with a list or dic
    needed_water = MENU[menu_item]['ingredients']['water']
    needed_milk = MENU[menu_item]['ingredients']['milk']
    needed_coffee = MENU[menu_item]['ingredients']['coffee']
    available_water = resources['water']
    available_milk = resources['milk']
    available_coffee = resources['coffee']
    #compare against resources
    if available_water < needed_water:
        print('Sorry there is not enough water.')
        return 'low water'
    elif available_milk < needed_milk:
        print('Sorry there is not enough milk.')
        return 'low milk'
    elif available_coffee < needed_coffee:
        print('Sorry there is not enough coffee.')
        return 'low milk'
    else:
        update_resources(needed_water,needed_milk,needed_coffee)
        return 'resources ok'
def update_resources(water_used,milk_used,coffee_used):
    resources['water']-= water_used
    resources['milk']-= milk_used
    resources['coffee']-= coffee_used


on = True
while on:
    coffee = choose_coffee()
    if coffee == 'off':
        on = False
    if on:
        #no need to check resources if the user hasnt paid enough
        enough_money = charge_for_coffee()
        if enough_money != 'no':
            resources_present = check_resources(coffee)
            if resources_present == 'resources ok':
                print(f'Here is your {coffee}. Enjoy! ☕')
