def stooge_sort(arr, low, high):
    if low >= high:
        return

    # If the first element is greater than the last, swap them
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]

    # If there are at least 3 elements in the subarray
    if high - low + 1 > 2:
        t = (high - low + 1) // 3

        # Recursively sort the first 2/3 of the array
        stooge_sort(arr, low, high - t)

        # Recursively sort the last 2/3 of the array
        stooge_sort(arr, low + t, high)

        # Recursively sort the first 2/3 of the array again
        stooge_sort(arr, low, high - t)

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#stooge_sort(my_list, 0, len(my_list) - 1)

#print("Sorted array (after Stooge Sort):", my_list)