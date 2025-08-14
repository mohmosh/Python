# Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. 
# We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. In order to accomplish this, we will need the following steps:

# Define the function to accept two input parameters called base and exponent
def largePower(base, exponent):
    
    # Calculate the result of base to the power of exponent
 result = base ** exponent

# Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False
 if result > 5000:
    return True
 else:
    return False

print(largePower(2, 3))     # False (8 is not > 5000)
print(largePower(10, 4))    # True (10000 is > 5000)

