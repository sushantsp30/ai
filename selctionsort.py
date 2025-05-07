print("selection sort\n\n")
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # Find the index of the minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr.copy())
print("Original array:", arr)
print("Sorted array:  ", sorted_arr)

