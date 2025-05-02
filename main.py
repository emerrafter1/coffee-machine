import machine_data

resources = machine_data.resources
menu = machine_data.MENU
money = 0
report ="""
"""




#TODO prompt user for input
machine_prompt = (input('What would you like? (espresso/latte/cappuccino):')).strip().lower()


#TODO Turn off coffee machine
coffee_machine_on = True

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
