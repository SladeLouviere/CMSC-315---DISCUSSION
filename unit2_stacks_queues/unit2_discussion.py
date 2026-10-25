"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        ## initializes and empty item list object 
        self.items = []
        return print ("New Stack created.\n")

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        ## Append adds the value to the end of the list, which represents the top of the stack, or first popped.
        print ("Appending...")
        self.items.append(value)
        return print (f"Appended: {value}\n")

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        ## if list is empty, pop throws error. try the pop and handling the 
            ## error if it occurs with a try/except block.
        print (f"Attempting pop...")
        try:
            value = self.items.pop()
            return print (f"Popped: {value}\n")
        except:
            return print ("Cannot pop from an empty stack.\n")

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        ## Peek looks at the top of the stack, 
            ## in this case, the last item in a list is found with [-1]
        print ("Taking a peek...")
        try:
            value = self.items[-1]
            return print (f"Top value: {value}\n")
        except:
            return print ("Stack is empty. Nothing to return.\n")

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        ## returns a bool if stack is ADT is empty (true) or not empty (false)
        print ("Checking stack is empty...")
        if len(self.items) == 0:
            return print ("Stack is empty.\n")
        return print (f"Stack initiated with {len(self.items)} item(s).\n")


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        ## Deque runtime complexity is O(1) or constant making it faster 
        self.queue = deque()
        return print ("New Queue created.\n")

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        ## Enqueue inserts at the back of a queue and dequeue removes the front value.
        self.queue.append(value)
        print (f"Enqueueing...")
        return print (f"Added to back: {value}\n")

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        ## if list is empty, dequeue throws error. try the dequeue and handling the error if it occurs with a try/except block.
        print (f"Attempting dequeue...")
        try:
            value = self.queue.popleft()
            return print (f"Removed front value: {value}\n")
        except:
            return print ("Cannot dequeue from an empty queue.\n")

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        ## front peeks at the value in the front position 
        print (f"Checking front value...")
        try:
            value = self.queue[0]
            return print (f"Front value: {value}\n")
        except:
            return print ("Queue is empty. Nothing to return\n")        

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        print ("Checking queue is empty...")
        if len(self.queue) == 0:
            return print ("Queue is empty.\n")
        return print (f"Queue initiated with {len(self.queue)} item(s).\n")


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")
print("      test popping from an empty stack,")
print("      test peeking at an empty stack,")
print("      and verify a single-item stack becomes empty after removal.")

print ()

print ("3. Improve the print statements so they clearly explain what is happening. (check methods)")
print ("1. Create a Stack object.")
MyStack = Stack()

print ("5. Show what happens when pop() is used on an empty stack.")
MyStack.pop()

print ("2. Add at least 4 values to the stack.")
MyStack.push(12)
MyStack.push(28)
MyStack.push(36)
MyStack.push(43)

print ("4. Demonstrate LIFO behavior.")
MyStack.peek()

MyStack.pop()
MyStack.pop()

MyStack.peek()

print ("6. Show what happens when peek() is used on an empty stack.")
MyStack.pop()
MyStack.pop()

MyStack.peek()

print ("7. Create a stack with 'only one item', remove it, and verify the stack is empty afterward.")
newStack = Stack()

newStack.push("only one item")

newStack.is_empty()

newStack.pop()

newStack.is_empty()


# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
print("      test dequeuing from an empty queue,")
print("      test viewing the front of an empty queue,")
print("      and verify a single-item queue becomes empty after removal.")

print ()

print ("3. Improve the print statements so they clearly explain what is happening. (check methods)")
print ("1. Create a Queue object.")
MyQueue = Queue()

print ("6. Show what happens when front() is used on an empty queue.")
MyQueue.front()

print ("2. Add at least 4 values to the queue.")
MyQueue.enqueue(24)
MyQueue.enqueue(85)
MyQueue.enqueue(93)
MyQueue.enqueue(67)

print ("4. Demonstrate FIFO behavior.")
MyQueue.front()

MyQueue.dequeue()
MyQueue.dequeue()

MyQueue.front()

print ("5. Show what happens when dequeue() is used on an empty queue.")
MyQueue.dequeue()
MyQueue.dequeue()

MyQueue.dequeue()

print ("7. Create a queue with 'only one item', remove it, and verify the queue is empty afterward.")
NewQueue = Queue()

NewQueue.enqueue("only one item")

NewQueue.is_empty()

NewQueue.dequeue()

NewQueue.is_empty()


if __name__ == "__main__":
    main()
