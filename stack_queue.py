# Class to represent a Stack with basic operations
class Stack:
    def __init__(self):
        # Initializes an empty stack using a list
        self.stack = []

    def push(self, value):
        # Pushes (adds) the value onto the stack
        self.stack.append(value)

    def pop(self):
        # Pops (removes) the top value from the stack
        if not self.is_empty():
            return self.stack.pop()  # Removes and returns the top value
        raise IndexError("Pop from an empty stack.")  # Raises an error if stack is empty

    def peek(self):
        # Returns the top value without removing it from the stack
        if not self.is_empty():
            return self.stack[-1]  # Returns the last element of the stack (top)
        raise IndexError("Peek from an empty stack.")  # Raises an error if stack is empty

    def is_empty(self):
        # Checks if the stack is empty
        return len(self.stack) == 0  # Returns True if stack is empty, else False

# Class to represent a Queue with basic operations
class Queue:
    def __init__(self):
        # Initializes an empty queue using a list
        self.queue = []

    def enqueue(self, value):
        # Enqueues (adds) the value to the end of the queue
        self.queue.append(value)

    def dequeue(self):
        # Dequeues (removes) the value from the front of the queue
        if not self.is_empty():
            return self.queue.pop(0)  # Removes and returns the first element
        raise IndexError("Dequeue from an empty queue.")  # Raises an error if queue is empty

    def peek(self):
        # Returns the front value without removing it from the queue
        if not self.is_empty():
            return self.queue[0]  # Returns the first element of the queue
        raise IndexError("Peek from an empty queue.")  # Raises an error if queue is empty

    def is_empty(self):
        # Checks if the queue is empty
        return len(self.queue) == 0  # Returns True if queue is empty, else False

# Example usage of the Stack class
stack = Stack()
stack.push(10)  # Pushes 10 onto the stack
stack.push(20)  # Pushes 20 onto the stack
print("Stack Pop:", stack.pop())  # Pops the top value from the stack (20)

# Example usage of the Queue class
queue = Queue()
queue.enqueue(10)  # Adds 10 to the end of the queue
queue.enqueue(20)  # Adds 20 to the end of the queue
print("Queue Dequeue:", queue.dequeue())  # Removes and returns the front value (10)
