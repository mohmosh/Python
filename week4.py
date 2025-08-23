# Open and write to a file named "jsMummies_contacts.pdf" in the "week4" directory.
file = open("jsMummies_contacts.pdf", "w")
file.write("jsMummie1, jsMummie2, jsMummie3")

# reading the content
file = open("jsMummies_contacts.pdf", "r")
content = file.read()
# print(content)