#  Challenge: Create a program that reads a text file, processes its content, and writes the results to a new file.

# 📌 Task Requirements:
# Create a file called input.txt and write at least five lines of text into it.
# Write a Python script to:
# Read the contents of input.txt.
# Count the number of words in the file.
# Convert all text to uppercase.
# Write the processed text and the word count to a new file called output.txt.
# Print a success message once the new file is created.

# Challenge: Create a program that reads a text file, processes its content, and writes the results to a new file.

# Create input.txt and write five lines
with open("input.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("Here is the second line.\n")
    file.write("The third line is right here.\n")
    file.write("Fourth line coming up!\n")
    file.write("Finally, this is the fifth line.\n")

# Step 1: Read the input file
with open("input.txt", "r") as infile:
    content = infile.read()   # ✅ use infile.read()

# Step 2: Count the number of words
words = content.split()
word_count = len(words)

# Step 3: Convert content to uppercase
uppercase_content = content.upper()

# Step 4: Write to output.txt
with open("output.txt", "w") as outfile:
    outfile.write("Processed Text:\n")
    outfile.write(uppercase_content + "\n\n")
    outfile.write(f"Word Count: {word_count}\n")

# Step 5: Print success message
print("✅ Processing complete! Results saved in output.txt")



