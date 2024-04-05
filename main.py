# TODO 1. Ask input of what the user wants to get
# TODO 2. Check availability and then if not available print the other options
# TODO 3. after the user chooses what they want, show them the price and ask them to insert the coins:
# TODO 4. if not enough return their return money and say "not enough money"
# TODO 5. Otherwise subtract only the amount needed to accomplish their request and give back the remainder
# TODO 6. Tell them to enjoy

from modules import MENU, resources


coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01,
}


def choose(option):
    if option == "espresso" or option == "latte" or option == "cappuccino": #maybe separate the expresso for it doesn't take milk
        if (resources["water"] >= MENU[option]["ingredients"]["water"]
                and resources["milk"] >= MENU[option]["ingredients"]["milk"]
                and resources["coffee"] >= MENU[option]["ingredients"]["coffee"]):
            resources["water"] -= MENU[option]["ingredients"]["water"]
            resources["milk"] -= MENU[option]["ingredients"]["milk"]
            resources["coffee"] -= MENU[option]["ingredients"]["coffee"]
            price_check(option)

        elif (resources["water"] > MENU[option]["ingredients"]["water"]
                and resources["coffee"] > MENU[option]["ingredients"]["coffee"]
              and resources["milk"] < MENU[option]["ingredients"]["milk"]
              and option == "espresso"):
            resources["water"] -= MENU[option]["ingredients"]["water"]
            resources["milk"] -= MENU[option]["ingredients"]["milk"]
            resources["coffee"] -= MENU[option]["ingredients"]["coffee"]
            price_check(option)

        elif (resources["coffee"] < MENU[option]["ingredients"]["coffee"]
              and resources["water"] < MENU[option]["ingredients"]["water"]
              and resources["milk"] < MENU[option]["ingredients"]["milk"]):
            print(f"Sorry unfortunately there are not enough resources to make your {option}.")

        elif (resources["coffee"] < MENU[option]["ingredients"]["coffee"]
              and resources["water"] < MENU[option]["ingredients"]["water"]):
            print(f"Sorry unfortunately there are not enough coffee and water resources to make your {option}.")

        elif (resources["coffee"] < MENU[option]["ingredients"]["coffee"]
              and resources["milk"] < MENU[option]["ingredients"]["milk"]):
            if option != "espresso":
                print(f"Sorry unfortunately there are not enough  coffee and milk to make your {option}.")
            else:
                print(f"Sorry unfortunately there are not enough coffee to make your {option}.")

        elif (resources["water"] < MENU[option]["ingredients"]["water"]
              and resources["milk"] < MENU[option]["ingredients"]["milk"]):
            if option != 'espresso':
                print(f"Sorry unfortunately there are not enough water and milk to make your {option}.")
            else:
                print(f"Sorry unfortunately there are not enough water to make your {option}.")

        elif resources["coffee"] < MENU[option]["ingredients"]["coffee"]:
            print(f"Sorry unfortunately there is not enough coffee to make your {option}.")

        elif resources["water"] < MENU[option]["ingredients"]["water"]:
            print(f"Sorry unfortunately there is not enough water to make your {option}.")

        elif resources["milk"] < MENU[option]["ingredients"]["milk"]:
            if option != 'espresso':
                print(f"Sorry unfortunately there is not enough milk to make your {option}.")
        run()
    elif option == "report":
        print(resources)
        run()
    elif option == "refill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        run()
    elif option == "off":
        return '\nThe machine is turning off'
    else:
        print("\nYou've inserted an invalid value. ")
        run()


def price_check(option):
    price = MENU[option]["cost"]
    print(f"The price for {option} is: ${price}\nPlease insert the coins.")
    quarter = int(input("\nHow many quarters?  "))
    dime = int(input("\nHow many dimes?  "))
    nickle = int(input("\nHow many nickles?  "))
    penny = int(input("\nHow many pennies?  "))

    quarters = quarter * coins["quarter"]
    dimes = dime * coins["dime"]
    nickles = nickle * coins["nickle"]
    pennies = penny * coins["penny"]
    sum_of_money = quarters + dimes + nickles + pennies

    if sum_of_money < price:
        print(f"Sorry but the money you've inserted is not enough.\nYou need more ${price - sum_of_money}.")
        run()
    else:
        change = sum_of_money - price
        if sum_of_money == price:
            print(f"\n\nThere you go your {option}. Enjoy!")
        else:
            print(f"\n\nThere you go your {option}. Enjoy!")
            print(f"And here is your change: {change}")


def run():
    choice = input("\nWhat would you like? (espresso/latte/cappuccino)  ").lower()
    yeah = choose(choice)
    return yeah


lets_go = run()
