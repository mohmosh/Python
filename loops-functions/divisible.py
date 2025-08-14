# Create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. 
# Using this, we can complete this function in a few steps:

# Define the function header to accept one input num
def divisible(num):
     
# Calculate the remainder of the input divided by 10 (use modulus)
 remainder = num % 10

# Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False
 if remainder == 0:
      return True
 else:
      return False
  
print(divisible(20))  # True
print(divisible(25))  # False