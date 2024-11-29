"""Create a function named calculate_discount(price, discount_percent) 
that calculates the final price after applying a 
discount. The function should take the original price
(price) and the discount percentage (discount_percent)
as parameters. If the discount is 20% or higher, apply the discount;
otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter 
the original price of an item and the discount percentage. Print the 
final price after applying the discount, or if no discount was applied, 
print the original price."""
"""discount_percent = int(input("Enter the discount:" ))
price = int(input("Enter the price:" ))
def calculate_discount(price, discount_percent):
    
    Final_price = discount_percent * price
    return Final_price;


if discount_percent >= 20 :
    print("apply Discount")
else:
    print("price")

Final_price = calculate_discount(price, discount_percent)
print( "Final_price")"""

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
    else:
        final_price = price
    return final_price

# Prompt the user to enter the original price and discount percentage
discount_percent = int(input("Enter the discount percentage: "))
price = float(input("Enter the original price: "))

# Calculate the final price using the function
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price based on the discount
print(f"The final price after applying the discount is: {final_price:.2f}")

    
