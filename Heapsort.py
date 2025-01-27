import time
import random
import matplotlib.pyplot as plt

# Heapsort Implementation
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify


def heapsort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (largest) with the last element
        heapify(arr, i, 0)


# Quicksort Implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Measure time for different input sizes
input_sizes = [10**3, 2 * 10**3, 5 * 10**3, 10**4]
heapsort_times = []
quicksort_times = []
mergesort_times = []

for size in input_sizes:
    array = [random.randint(0, 10**6) for _ in range(size)]
    
    # Heapsort
    start = time.time()
    heapsort(array.copy())
    heapsort_times.append(time.time() - start)
    
    # Quicksort
    start = time.time()
    quicksort(array.copy())
    quicksort_times.append(time.time() - start)
    
    # Merge Sort
    start = time.time()
    merge_sort(array.copy())
    mergesort_times.append(time.time() - start)

# Plot the results
plt.plot(input_sizes, heapsort_times, label="Heapsort")
plt.plot(input_sizes, quicksort_times, label="Quicksort")
plt.plot(input_sizes, mergesort_times, label="Merge Sort")
plt.xlabel("Input Size")
plt.ylabel("Time (s)")
plt.title("Heapsort vs Quicksort vs Merge Sort")
plt.legend()
plt.show()