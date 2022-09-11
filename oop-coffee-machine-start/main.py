from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
OFF = False
CoffeeMachine = CoffeeMaker()
MoneyMaker = MoneyMachine()
Orders = Menu()


while not OFF:

    # TODO: 1.Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    choice = input("What would you like? (espresso/latte/cappuccino/chococcino):").lower()

    # TODO: 2.Turn off the coffee machine by entering "OFF" on the prompt.
    if choice == "off":
        OFF = True

    # TODO: 3.Print report.
    elif choice == "report":
        CoffeeMachine.report()
        MoneyMaker.report()

    # TODO: 4. Check resources sufficient?
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino" or choice == "chococcino":
        selected_drink = Orders.find_drink(choice)
        enough_resources = CoffeeMachine.is_resource_sufficient(selected_drink)

    # TODO: 5. Process coins.
        if enough_resources:

            # TODO: 6. Check transaction successful?
            payment_successful = MoneyMaker.make_payment(selected_drink.cost)

            # TODO: 7. Make Coffee.
            if payment_successful and enough_resources:
                CoffeeMachine.make_coffee(selected_drink)
