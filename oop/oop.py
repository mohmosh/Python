# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.
# Activity 2: Polymorphism Challenge! 🎭

# Parent Class
class Book:
    def __init__(self, title, author, genre):
        self.title = title        # attribute
        self.author = author
        self.genre = genre

    def read(self):
        print(f"You're reading '{self.title}' by {self.author}. It's a {self.genre} book.")

# Child Class (Inheritance)
class Ebook(Book):
    def __init__(self, title, author, genre, file_size):
        super().__init__(title, author, genre)  # Call parent constructor
        self.file_size = file_size

    def download(self):
        print(f"Downloading '{self.title}'... ({self.file_size}MB)")





# Create a program that includes animals or vehicles with the same action (like move()). However,
# make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

# Parent class
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Subclass 1
class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️")

# Subclass 3
class Boat(Vehicle):
    def move(self):
        print("The boat is sailing 🚢")

