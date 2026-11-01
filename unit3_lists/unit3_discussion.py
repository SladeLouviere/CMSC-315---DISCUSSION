"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
## Insert adds the new value at the specified position.
## Existing elements at that position and after it shift one position to the 
    # right to make room.
## Inserting at the beginning or middle requires shifting existing elements, 
    # so it can take O(n) time.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
## Validate the index before attempting deletion. Negative indexes are valid in Python 
    # if they are within the list's range 
    if index < -len(lst) or index >= len(lst):
        return None
## pop() removes the element and returns its value. Elements after the deleted 
    # position shift left.
    return lst.pop(index)
   

def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
## This is a linear search because it may need to examine every element until 
    # the value is found.
##  Its worst-case time complexity is O(n).
    try:
        return list.index(lst, value)
    except ValueError:
        return -1

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # Creates a list containing several books.
    bookList = ["It", "Jaws", "Becoming"]

    # Displays the original list.
    print("\n--- Original list ---")
    print(bookList)

    # Inserts a book at the beginning (index 0).
    # Existing elements shift one position to the right.
    insert_at(bookList, 0, "The Hobbit")
    print("\n--- After beginning insertion ---")
    print(bookList)

    # Inserts a book in the middle (index 2).
    # Elements at index 2 and beyond shift right.
    insert_at(bookList, 2, "Dune")
    print("\n--- After middle insertion ---")
    print(bookList)

    # Inserts a book at the end.
    # No existing elements need to shift.
    insert_at(bookList, len(bookList), "Moby Dick")
    print("\n--- After end insertion ---")
    print(bookList)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # Deletes the first book (index 0).
    removed = delete_at(bookList, 0)
    print(f"\nRemoved from beginning: {removed}")
    print("Updated list:", bookList)

    # Deletes a book from the middle.
    removed = delete_at(bookList, 1)
    print(f"\nRemoved from middle: {removed}")
    print("Updated list:", bookList)

    # Deletes the last book.
    removed = delete_at(bookList, -1)
    print(f"\nRemoved from end: {removed}")
    print("Updated list:", bookList)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # Searches for a book that exists.
    search = search_value(bookList, "The Hobbit")

    if search != -1:
        print(f"The Hobbit was found at index {search}.")
    else:
        print("The Hobbit was not found.")

    # Searches for a book that does not exist.
    search = search_value(bookList, "Jaws")

    if search != -1:
        print(f"Jaws was found at index {search}.")
    else:
        print("Jaws was not found.")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

## EDGE CASE: Insert into an empty list.
## Python allows inserting to empty lists. The new value becomes the first element.
    emptyList = []

    insert_at(emptyList, 32, "Harry Potter")

    print("\n1. Inserting into an empty list:")
    print(emptyList)

## EDGE CASE: Delete using an invalid index.
## The list contains only one element, so index 5 does not exist.
    removed = delete_at(emptyList, 5)

    print("\n2. Deleting using an invalid index:")
    print("Removed value:", removed)

## EDGE CASE: Search for a missing value.
## The value "Twilight" is not in the list. search_value() should return -1.
    search = search_value(emptyList, "Twilight")

    print("\n3. Searching for a missing value:")
    if search == -1:
        print("Book not found. Returned -1.")
    else:
        print("Book found at index", search)


if __name__ == "__main__":
    main()