def gnome_sort(arr):
    i = 0
    n = len(arr)

    while i < n:
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            # Swap the elements and move one step back
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#gnome_sort(my_list)

#print("Sorted array (after Gnome Sort):", my_list)