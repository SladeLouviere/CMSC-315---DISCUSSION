# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.


<!-- Reflection -->
While completing this assignment, I learned how a BST organizes data and how recursive methods can be used to insert, search, and retrieve values. I also learned how an in-order traversal visits the left subtree, current node, and right subtree to display values in ascending order.

One challenge I encountered was understanding how recursion returns the correct node references during insertion. I am still accustomed to Java's direct data typing and variable declarations during initialization, so adjusting to Python's syntax and dynamic typing took some getting used to. I worked through these challenges by testing different scenarios and adding comments to explain how each operation worked.

For my real-world application, I designed a library inventory system that used ISBN numbers to organize books. Smaller ISBN numbers were placed in the left subtree, while larger numbers were placed in the right subtree. I also considered how each ISBN could serve as the key for a book object containing additional information, such as the author's name, book title, genre, and location within the library. This would allow the library to search by ISBN and retrieve the book's other identifying information. I used in-order traversal to display the ISBN numbers in sorted order. 

A BST can improve search efficiency because each comparison eliminates part of the tree. A balanced BST can search in O(log n) time, compared to O(n) for a linear search. However, an unbalanced BST can also take O(n) time. This assignment helped me understand how BSTs can be useful for organizing and retrieving information.

<!-- IMPLEMENTATION -->

I designed my Binary Search Tree around a library inventory system using ISBN numbers to organize books. I inserted each ISBN so that smaller values were placed in the left subtree and larger values were placed in the right subtree. This allowed me to search for specific books efficiently without checking every ISBN individually. I also used in-order traversal to display the ISBNs in ascending order. My application demonstrated how a BST could help a library organize its book inventory and quickly locate books by their identification numbers. 