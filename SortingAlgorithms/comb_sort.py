def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink_factor = 1.3
    swapped = True

    while gap > 1 or swapped:
        # Update the gap using the shrink factor
        gap = max(1, int(gap / shrink_factor))

        # Reset the swapped flag
        swapped = False

        # Compare elements with a gap
        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#comb_sort(my_list)

#print("Sorted array (after Comb Sort):", my_list)