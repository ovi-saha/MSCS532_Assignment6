# Class to represent an Array with basic operations
class Array:
    def __init__(self):
        # Initializes an empty array
        self.data = []

    def insert(self, value, index=None):
        # If no index is specified, append the value at the end of the array
        if index is None:
            self.data.append(value)
        else:  # If an index is provided, insert the value at the specified index
            self.data.insert(index, value)

    def delete(self, index):
        # Deletes the value at the specified index
        if 0 <= index < len(self.data):  # Ensure index is within bounds
            return self.data.pop(index)  # Removes and returns the value
        raise IndexError("Index out of range.")  # Raise an error if index is invalid

    def access(self, index):
        # Access the value at the specified index
        if 0 <= index < len(self.data):  # Ensure index is within bounds
            return self.data[index]
        raise IndexError("Index out of range.")  # Raise an error if index is invalid

# Class to represent a Matrix with basic operations
class Matrix:
    def __init__(self, rows, cols):
        # Initializes a matrix with the specified number of rows and columns
        # All values are initialized to 0
        self.matrix = [[0] * cols for _ in range(rows)]

    def insert(self, row, col, value):
        # Inserts a value at the specified row and column
        self.matrix[row][col] = value

    def access(self, row, col):
        # Accesses the value at the specified row and column
        return self.matrix[row][col]

    def display(self):
        # Displays the matrix row by row
        for row in self.matrix:
            print(row)

# Example usage of the Array class
array = Array()
array.insert(10)  # Adds 10 to the end of the array
array.insert(20)  # Adds 20 to the end of the array
array.insert(30, 1)  # Inserts 30 at index 1
print("Array:", array.data)  # Displays the array contents
array.delete(1)  # Deletes the value at index 1
print("After Deletion:", array.data)  # Displays the array after deletion

# Example usage of the Matrix class
matrix = Matrix(2, 3)  # Creates a 2x3 matrix initialized with 0s
matrix.insert(0, 1, 5)  # Inserts 5 at row 0, column 1
# Displays the matrix
print("Matrix:")
matrix.display()

