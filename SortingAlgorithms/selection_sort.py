def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Find the minimum element in the remaining unsorted part
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#selection_sort(my_list)

#print("Sorted array (after Selection Sort):", my_list)