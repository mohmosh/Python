# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount.
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

# The function
def calculate_discount(price, discount_percent):
    
    # If the discount is 20%
    if discount_percent >= 20:
        # calculate the discount
        discount_amount = price * (discount_percent / 100)
           # subtract discount from price and return final price
        return price - discount_amount
        
        #  otherwise, return the original price.
    else:
        return price   
    
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
    
    # Call the function 
final_price = calculate_discount(price, discount_percent)
# and print the result
print(f"The final price after discount is: {final_price}")
  