# Create a program that asks for the user’s name and favorite color, 
# then prints a personalized greeting like: “Hello, [Name]! Your favorite color, [Color], is awesome!”

user = input("What is your name?")

color = input("What is your favourite color? ")

# f"Hello, {user}!" is an f-string that allows you to embed variables directly.
print(f"Hello,{user}! Your favourite color, {color}, is awesome!")


# Another example of a simple program that interacts with the user:
name = input("What is your name? ")

age = int(input("How old are you? "))

print(f"Hello, {name}! You are {age} years old.")
