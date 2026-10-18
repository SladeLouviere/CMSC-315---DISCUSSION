"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.


class Book:

    category = "General"

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"{self.title} by {self.author}, published {self.year}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class FictionBook(Book):

    category = "Fiction"

    def __init__(self, title, author, year, genre, age_rating):
        super().__init__(title, author, year)

        # Two new instance variables
        self.genre = genre
        self.age_rating = age_rating

    # New Method
    def recommend(self):
        print(f"Recommend for fans of {self.genre} books!\n")

    # Override the parent's method
    def display_info(self):
        return super().display_info() + f" is a {self.genre} book for ages {self.age_rating} and up\n"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    # Create 2 child-class objects
    book1 = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "realistic fiction", 14)

    book2 = FictionBook("Lord of the Flies", "William Golding", 1954, "fiction", 12)

    # Access class variable through the class
    print("Class variable: " , FictionBook.category)

    # Access class variable through an object
    print("Object class variable: " , book1.category)

    # Add attribute to only one object
    book1.pages = 180

    # Display each object class namespaces
    print("\nBook 1 namespace:")
    print(book1.__dict__)

    print("\nBook 2 namespace:")
    print(book2.__dict__)

    # Display child class namespace
    print("\nFictionBook Namespace")
    print(FictionBook.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    # Create an object with nested mutable data
    book1 = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "fiction", 14)

    book1.tags = ["classic", "american-literature", "tragedy", "romance"]

    # Create a shallow copy with a reference to the tags 
    shallow_book = copy(book1)

    # Create a deep copy with its own tags
    deep_book = deepcopy(book1)

    book1.tags.append("good read")

    # Display original, shallow copy, and deep copy
    print("\nbook1 namespace: ")
    print(book1.__dict__)
    
    print("\nshallow_book namespace: ")
    print(shallow_book.__dict__)
    
    print("\ndeep_book namespace: ")
    print(deep_book.__dict__)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===\n")

    print("\nTODO: Create and test your parent object")
    print("\n=== Parent Class ===")

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    print(book1.display_info())

    print("\nTODO: Create and test your child object")
    print("\n=== Child Class ===")

    book2 = FictionBook("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 10)
    print(book2.display_info())
    book2.recommend()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()