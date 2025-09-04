MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}
def checking_resources(drink):
    if drink == "report":
        print(resources)
        return False

    for key in resources:
        if key in MENU[drink]["ingredients"]:
            if resources[key] < MENU[drink]["ingredients"][key]:
                print(f"Sorry there is not enough {key}")
                return False
            else:
                resources[key] -= MENU[drink]["ingredients"][key]
    return True

def checking_money(drink, money):
    if money >= MENU[drink]["cost"]:
        if "money" not in resources:
            resources["money"] = 0.0
        resources["money"] += MENU[drink]["cost"]
        return round(money - MENU[drink]["cost"] , 1)
    else:
        return False

def coffee_machine():
    working = True
    while working:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if checking_resources(drink):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
            result = checking_money(drink, money)
            if result == False:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is ${result} in change.")
                print(f"Here is your {drink} ☕. Enjoy! ")

coffee_machine()