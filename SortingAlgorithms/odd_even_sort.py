def odd_even_sort(arr):
    n = len(arr)
    sorted = False

    while not sorted:
        sorted = True

        # Perform odd-phase sorting
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

        # Perform even-phase sorting
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#odd_even_sort(my_list)

#print("Sorted array (after Odd-Even Sort):", my_list)