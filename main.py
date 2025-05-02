import machine_data

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
        for ingredient in menu[machine_prompt]["ingredients"]:
            if menu[machine_prompt]["ingredients"][ingredient] > resources[ingredient]:
                print(f"Sorry there is not enough {ingredient.lower()}")
