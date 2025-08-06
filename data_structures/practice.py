# LIST
# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
user_input = input("Give me a list of numbers seperated by space: ")

# Split the input into a list of strings and convert each to an integer
integer_list = [int(num) for num in user_input.split()]

# The sum of the numbers in the list
total_sum = sum(integer_list)

print("The sum of the numbers is:" , total_sum)

# TUPLE
# Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
favourite_books = ("The river between", "The Alchemist", "The Bible", "The Gurdian Angel", "The Secret")

# A for loop to print each book in a line
for book in favourite_books:
    print(book)

    # DICTIONARY
    # Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for
    # input and store the information in the dictionary. Then, print the dictionary to the cons
    
    # create an empty dictionary
    person = {}
    
# get the user input
person['name'] = input("What is your name? ")
person['age'] = input("What is your age? ")
person['favorite_color'] = input("What is your favorite color? ")

# print the dictionary
print("\nPerson's Information:")
print(person)

# SETS
# Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.
input1 = input("Enter a set of numbers seperated by commas: ")
set1 = set(int(num) for num in input1.split(","))

input2 = input("Enter another set of numbers seperated by commas: ")
set2 = set(int(num) for num in input2.split(","))
  
# Find the common elements
common_numbers = set1 & set2
print("The common numbers in both sets are:", common_numbers)

# LISTS
# Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that 
# have an odd number of characters.

# list to store words
words = ["Hen", "Goat", "Elephant", "Dog", "Cat", "Mouse"]

# Use list comprehension to filter words with odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Original words:", words)
print("Words with odd number of characters:", odd_length_words)