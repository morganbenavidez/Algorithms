def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1

    while (swapped == True):
        # Reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # swap if no swap happened inside the loop
        swapped = False

        # Loop from left to right, similar to the bubble sort
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # If no swap happened, the list is already sorted
        if (swapped == False):
            break

        # Move the end point back by one, because
        # the item at the end is in its rightful spot
        end = end-1

        # Reset the swapped flag
        swapped = False

        # Move from right to left
        for i in range(end-1, start-1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Increase the starting point because
        # the last item is in its rightful spot
        start = start + 1

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#cocktail_sort(my_list)

#print("Sorted array (after Cocktail Sort):", my_list)