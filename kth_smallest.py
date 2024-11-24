import random
import time

# Function to find the median of a small group
def find_median(arr):
    arr.sort()
    return arr[len(arr) // 2]

# Deterministic Median of Medians algorithm
def median_of_medians(arr, k):
    # Base case: If the array is small, sort and return the k-th element
    if len(arr) <= 5:
        arr.sort()
        return arr[k]

    # Step 1: Divide the array into groups of 5 and find medians
    medians = [find_median(arr[i:i + 5]) for i in range(0, len(arr), 5)]

    # Step 2: Recursively find the median of medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Step 3: Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(low) - len(high)  # Count occurrences of the pivot

    # Step 4: Determine the k-th smallest element
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return median_of_medians(high, k - len(low) - pivot_count)

# Randomized Quickselect algorithm
def randomized_quickselect(arr, k):
    # Base case: If the array has only one element
    if len(arr) == 1:
        return arr[0]

    # Step 1: Pick a random pivot
    pivot = random.choice(arr)

    # Step 2: Partition the array
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(low) - len(high)  # Count occurrences of the pivot

    # Step 3: Determine the k-th smallest element
    if k < len(low):
        return randomized_quickselect(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return randomized_quickselect(high, k - len(low) - pivot_count)

# Function to generate different array types
def generate_arrays(arr):
    random_arr = random.sample(range(1, len(arr) * 2), len(arr))  # Random array with unique values
    sorted_arr = sorted(arr)
    reverse_sorted_arr = sorted_arr[::-1]
    return random_arr, sorted_arr, reverse_sorted_arr

# User interaction and timing for different arrays
def main():
    print("Enter the array elements separated by spaces:")
    arr = list(map(int, input().split()))  # User input array
    print("Enter the value of k (1-based index):")
    k = int(input()) - 1  # Convert to 0-based index
    print(f"\nInput Array: {arr}")
    
    # Generate random, sorted, and reverse-sorted arrays from the user input array
    random_arr, sorted_arr, reverse_sorted_arr = generate_arrays(arr)
    
    # # Generate random array from the user input array
    # random_arr = generate_arrays(arr)
    print(f"\nGenerated Random Array: {random_arr}")

    # Function to run and print results for both algorithms
    def run_algorithm(arr, array_type):
        print(f"\n--- Testing with {array_type} Array ---")

        # Deterministic algorithm execution
        start_time = time.time()
        deterministic_result = median_of_medians(arr.copy(), k)
        deterministic_time = time.time() - start_time
        print(f"The {k + 1}-th smallest element is: {deterministic_result}")
        print(f"Time taken (Deterministic): {deterministic_time:.6f} seconds")

        # Randomized algorithm execution
        start_time = time.time()
        randomized_result = randomized_quickselect(arr.copy(), k)
        randomized_time = time.time() - start_time
        print(f"The {k + 1}-th smallest element is: {randomized_result}")
        print(f"Time taken (Randomized): {randomized_time:.6f} seconds")

    # Run tests for the user input array, random, sorted, and reverse-sorted arrays
    run_algorithm(arr, "User-Input")
    run_algorithm(random_arr, "Random")
    run_algorithm(sorted_arr, "Sorted")
    run_algorithm(reverse_sorted_arr, "Reverse-Sorted")

if __name__ == "__main__":
    main()