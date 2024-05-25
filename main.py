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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_enough_resources(order_ingredients):
    """Returns True when the machine has enough resources to make the order,
    and False if the ingredients are not enough"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry. There's not enough {item}. ")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many five-cent coins?")) * 0.05
    total += int(input("How many ten-cent coins?")) * 0.10
    total += int(input("How many twenty-cent coins?")) * 0.20
    total += int(input("How many fifty-cent coins?")) * 0.50
    total += int(input("How many one-euro coins?")) * 1.00
    total += int(input("How many two-euro coins?")) * 2.00
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False is not enough money"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Your change is {change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money")
        return False


def make_coffe(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
        print("A máquina foi desligada!")
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(f"Your {choice} costs {drink["cost"]}")
        if is_enough_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])


