# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?


<!-- Reflection -->
Completing this assignment helped me better understand Python lists, including how to insert, delete, and search. I also improved my understanding of positive and negative indexing, index validation, and handling edge cases like inserting into empty lists and deleting items that don't exist.

One challenge I encountered was understanding how Python handles indexes outside a list's range. Initially, I thought insertion and deletion worked the same way when dealing with invalid indexes. After testing different scenarios and reviewing how the built-in methods behave, I learned that insertion automatically adjusts out-of-range indexes, while deletion requires validation to prevent errors.

List operations can impact performance in real-world applications, especially when working with large amounts of data. For example, if I used a list to store the Book objects from my Unit 1 discussion, inserting or deleting books near the beginning of a Library's list would require the other elements to shift positions. This takes additional processing time, especially as the library grows and contains more and more books. Understanding these performance differences can help developers choose more efficient ways to organize, store, and manage data.