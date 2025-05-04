def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is at current index
        min_index = i
        for j in range(i+1, n):
            # Greedy choice: find the minimum in the unsorted part
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap with the current index
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
data = [64, 25, 12, 22, 11]
sorted_data = selection_sort(data)
print("Sorted array using Greedy Selection Sort:")
print(sorted_data)
