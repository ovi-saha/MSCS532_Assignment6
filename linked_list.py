# Class to represent a Node in the LinkedList
class Node:
    def __init__(self, value):
        # Each Node has a value and a reference (pointer) to the next Node
        self.value = value
        self.next = None  # Initially, the next node is set to None

# Class to represent the LinkedList
class LinkedList:
    def __init__(self):
        # The LinkedList starts with no elements, so the head is None
        self.head = None

    def insert(self, value):
        # Creates a new node with the given value
        new_node = Node(value)
        if not self.head:  
            # If the list is empty, the new node becomes the head
            self.head = new_node
        else:
            # Otherwise, traverse the list to find the last node
            current = self.head
            while current.next:  # Continue until the last node is reached
                current = current.next
            # Append the new node to the end of the list
            current.next = new_node

    def delete(self, value):
        # Deletes the first occurrence of the node with the specified value
        if not self.head:  
            # If the list is empty, there's nothing to delete
            return None

        if self.head.value == value:  
            # If the head node holds the value to delete
            self.head = self.head.next  # Move the head to the next node
            return

        # Traverse the list to find the node to delete
        current = self.head
        while current.next and current.next.value != value:  
            # Continue until the desired value is found or the end of the list is reached
            current = current.next

        if current.next:  
            # If the node to delete is found, skip it by updating the next pointer
            current.next = current.next.next

    def traverse(self):
        # Prints all the nodes in the list in order
        current = self.head
        while current:  
            # Continue until the end of the list
            print(current.value, end=" -> ")  # Print the value of the current node
            current = current.next  # Move to the next node
        print("None")  # Indicate the end of the list

# Example usage of the LinkedList
linked_list = LinkedList()

# Insert values into the LinkedList
linked_list.insert(10)  # Insert 10 as the first node
linked_list.insert(20)  # Insert 20 at the end of the list
linked_list.insert(30)  # Insert 30 at the end of the list

# Traverse the LinkedList and display its contents
linked_list.traverse()  # Output: 10 -> 20 -> 30 -> None

# Delete a node with the value 20 from the LinkedList
linked_list.delete(20)

# Traverse the LinkedList again to see the updated contents
linked_list.traverse()  # Output: 10 -> 30 -> None
