"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.right_child = None
        self.left_child = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        if self.root == None:
            self.root = Node(value)
            return self.root
        else:
            return self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # A BST keeps smaller values in the left subtree and larger
        #   values in the right subtree. This ordering helps determine
        #   which direction to follow when inserting a new value.
        # Duplicate values are not added to the BST, they are neither < nor >.
        if value < node.value:
            if node.left_child == None:
                node.left_child = Node(value)
                return node
            else:
                return self._insert_recursive(node.left_child, value)
        elif value > node.value:
            if node.right_child == None:
                node.right_child = Node(value)
                return node
            else:
                return self._insert_recursive(node.right_child, value)
        else:
            return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST searching is often more efficient than linear searching
        #   because each comparison eliminates an entire subtree.
        #   In a balanced BST, this makes searching O(log n), compared
        #   to O(n) for a linear search. An unbalanced BST can take O(n).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node == None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left_child, value)
        return self._search_recursive(node.right_child, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        return self._inorder_recursive(self.root, values)

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node == None:
            return values
        # In a BST, values in the left subtree are smaller than the
        #   current node, while values in the right subtree are larger.
        #   Visiting left, current, then right therefore produces
        #   values in ascending sorted order.
        self._inorder_recursive(node.left_child, values)
        values.append(node.value)
        self._inorder_recursive(node.right_child, values)
        return values


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    # print("TODO: Create a BST and insert multiple values.")

    library_tree = BST()
    print("\nBinary Search Tree created")

    isbn_numbers = [
    9780143127741,
    9780439023528,
    9780061120084,
    9780316769488,
    9780547928227,
    9780307474278,
    9780451524935
    ]
    
    print(f"\nValues being inserted:")
    for value in isbn_numbers:
        # Each comparison determines whether to explore the left or right
        #   subtree, reducing the number of nodes that need to be checked.
        library_tree.insert(value)
        print(value, end=" ")
    print()

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    # print("TODO: Display and explain traversal results.")

    # In-order traversal visits the left subtree, current node,
    #   and right subtree. Because of the BST ordering rule,
    #   the resulting list is sorted in ascending order.
    print(f"\nValues in-order:")
    for order in library_tree.inorder():
        print(order, end=", ")
    print()


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # print("TODO: Demonstrate BST searching.")

    search_values = [9780061120084, 9780316769488, 9780061120087, 9780316769481]
    print(f"\nSearch Values - 9780061120084, 9780316769488, 9780061120087, 9780316769481 respectively")

    # The first two ISBNs exist in the BST, so their searches return True.
    # The last two ISBNs do not exist, so their searches return False.
    for value in search_values:
        # each comparison determines which subtree to explore, 
        #   rather than checking every node
        print(library_tree.search(value), end=" ")
    print()

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    # print("TODO: Demonstrate and explain an edge case.")


    empty_tree = BST()
    # inorder() calls the recursion, but since the root node is none,
    #   the base result returns the values list which is empty
    print(f"\nTraverse empty BST:\n{empty_tree.inorder()}")

    # search() calls the recursion, but since the root node is none,
    #   the base result returns False
    print(f"\nSearch empty BST\n{empty_tree.search(22)}")

    # the FIRST insert() sets the Node(22) as the root
    # the SECOND insert() calls the recursion on the root node, 
    #   since the values are the same, it returns the current node, aka the root
    print(f"\nInsert duplicates to BST")
    empty_tree.insert(22)
    empty_tree.insert(22)
    print(f"Inserted 22 twice. BST in-order output: {empty_tree.inorder()}\n")


if __name__ == "__main__":
    main()