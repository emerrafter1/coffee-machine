import machine_data
import math

resources = machine_data.resources
menu = machine_data.MENU
money = 0
report ="""
"""

#TODO Turn off coffee machine
coffee_machine_on = True

while coffee_machine_on == True:


    #TODO prompt user for input
    machine_prompt = (input('What would you like? (espresso/latte/cappuccino):')).strip().lower()

    if machine_prompt == "off":
        coffee_machine_on = False

    if machine_prompt == "report":
        resources["money"] = money
        for item in resources:
            name = item.title()
            amount = resources[item]

            if name == "Coffee":
                report += f"{name}: {amount}g\n"
            elif name == "Money":
                report += f"{name}: ${amount}\n"
            else:
                report += f"{name}: {amount}ml\n"

        print(report)

    #TODO check resource sufficiency
    if machine_prompt == "espresso" or machine_prompt == "latte" or machine_prompt == "cappuccino":

        enough_resources = True

        for ingredient in menu[machine_prompt]["ingredients"]:
            if menu[machine_prompt]["ingredients"][ingredient] > resources[ingredient]:
                enough_resources: False
                print(f"Sorry there is not enough {ingredient.lower()}")

        if enough_resources:
            coffee_cost = menu[machine_prompt]['cost']
            quarters = int(input(f"The cost of this coffee is ${round(coffee_cost, 2)}. Please insert coins.\nHow many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total_paid = (quarters*0.25) + (dimes*0.1) + (nickles*0.05)+(pennies*0.01)

            if total_paid < coffee_cost:
                print("Sorry that's not enough money. Money refunded.")
            elif total_paid > coffee_cost:
                change = total_paid - coffee_cost
                print(f"Here is ${round(change,2)} dollars in change.")
                money += coffee_cost
            else:
                money += coffee_cost



