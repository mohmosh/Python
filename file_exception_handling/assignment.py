# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

# Write
with open("assignment.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("Here is the second line.\n")
    file.write("The third line is right here.\n")
    
    # read
with open("assignment.txt", "r") as infile:
    conten = infile.read()
    
    
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be 
filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as infile:
        content = infile.read()
        print("File content successfully read.")
        
except FileNotFoundError:
        print("File not found. Check the filename and try again")
