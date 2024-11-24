# Class to represent a tree node with multiple children
class TreeNode:
    def __init__(self, value):
        # Initializes a node with a given value and an empty list of children
        self.value = value
        self.children = []  # Each node can have multiple children (list of child nodes)

    def add_child(self, child_node):
        # Adds a child node to the current node's list of children
        self.children.append(child_node)

    def display(self, level=0):
        # Displays the node's value, with indentation based on its level in the tree
        print("  " * level + str(self.value))  # Indentation is based on the 'level' parameter
        # Recursively displays all child nodes
        for child in self.children:
            child.display(level + 1)  # Increment the level for child nodes

# Example usage
root = TreeNode(1)  # Create the root node with value 1
child1 = TreeNode(2)  # Create a child node with value 2
child2 = TreeNode(3)  # Create a child node with value 3

root.add_child(child1)  # Add child1 as a child of root
root.add_child(child2)  # Add child2 as a child of root

child1.add_child(TreeNode(4))  # Add a child node with value 4 to child1
child1.add_child(TreeNode(5))  # Add a child node with value 5 to child1

root.display()  # Display the tree structure starting from the root