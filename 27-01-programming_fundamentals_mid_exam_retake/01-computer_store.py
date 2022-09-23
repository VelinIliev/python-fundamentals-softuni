total_without_taxes = 0
type_of_order = ""

while True:
    command = input()
    if command == "special" or command == "regular":
        type_of_order = command
        break
    else:
        price_wo_tax = float(command)
        if price_wo_tax < 0:
            print("Invalid price!")
        else:
            total_without_taxes += price_wo_tax

#
if total_without_taxes == 0:
    print("Invalid order!")
else:
    taxes = total_without_taxes * .2
    if type_of_order == "special":
        final_price = (total_without_taxes + taxes) * .9
    else:
        final_price = total_without_taxes + taxes

    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_without_taxes:.2f}$')
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    print(f'Total price: {final_price:.2f}$')
#
#
# Write a program that prints you a receipt for your new computer. You will
# receive the parts' prices (without tax) until you receive what type of
# customer this is - special or regular. Once you receive the type of customer
# you should print the receipt.
# The taxes are 20% of each part's price you receive.
# If the customer is special, he has a 10% discount on the total price with taxes.
# If a given price is not a positive number, you should print "Invalid price!"
# on the console and continue with the next price.
# If the total price is equal to zero, you should print "Invalid order!" on the console.
# Input
# •	You will receive numbers representing prices (without tax) until command
# "special" or "regular":
# Output
# •	The receipt should be in the following format:
# "Congratulations you've just bought a new computer!
# Price without taxes: {total price without taxes}$
# Taxes: {total amount of taxes}$
# -----------
# Total price: {total price with taxes}$"
# Note: All prices should be displayed to the second digit after the decimal
# point! The discount is applied only on the total price. Discount is only
# applicable to the final price!
