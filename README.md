# Coffee Machine Program Requirements

1. **Prompt user for drink selection**

   - Ask:  
     `What would you like? (espresso/latte/cappuccino):`
   - Check user input to decide what to do next.
   - The prompt should appear again after each action (e.g., once the drink is dispensed) to serve the next customer.

2. **Turn off the coffee machine**

   - Enter `"off"` to shut down the machine.
   - `"off"` is the secret word for maintainers to turn it off.
   - Program execution ends when `"off"` is entered.

3. **Print a report**

   - Enter `"report"` to generate a status report showing current resources:

     ```
     Water: 100ml
     Milk: 50ml
     Coffee: 76g
     Money: $2.5
     ```

4. **Check resource sufficiency**

   - When a drink is chosen, check if enough resources are available.
   - Example:  
     If a latte requires 200ml water but only 100ml is available, print:

     ```
     Sorry there is not enough water.
     ```

   - Same for other depleted resources (milk, coffee).

5. **Process coins**

   - If enough resources, prompt user to insert coins.
   - Coin values:
     - Quarters = $0.25
     - Dimes = $0.10
     - Nickels = $0.05
     - Pennies = $0.01
   - Calculate total inserted. Example:

     ```
     1 quarter, 2 dimes, 1 nickel, 2 pennies
     = 0.25 + (0.10 × 2) + 0.05 + (0.01 × 2)
     = $0.52
     ```

6. **Check transaction success**

   - Confirm if inserted money is sufficient:
     - Example:  
       If a latte costs $2.50 but only $0.52 inserted:

       ```
       Sorry that's not enough money. Money refunded.
       ```

   - If enough money:
     - Add drink cost to machine's profit.
     - Example updated report:

       ```
       Water: 100ml
       Milk: 50ml
       Coffee: 76g
       Money: $2.5
       ```

   - If too much money:
     - Offer change:

       ```
       Here is $2.45 dollars in change.
       ```

     - Change should be rounded to 2 decimal places.

7. **Make coffee**

   - If transaction is successful and resources are sufficient:
     - Deduct ingredients from resources.
     - Example report **before** purchasing a latte:

       ```
       Water: 300ml
       Milk: 200ml
       Coffee: 100g
       Money: $0
       ```

     - Report
