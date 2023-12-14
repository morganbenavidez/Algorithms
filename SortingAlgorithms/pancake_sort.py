def pancake_sort(arr):
    def flip(sublist_end):
        # Reverse the sublist from index 0 to sublist_end
        arr[:sublist_end + 1] = reversed(arr[:sublist_end + 1])

    n = len(arr)

    # Start from the last element and move towards the first
    for curr_size in range(n, 1, -1):
        # Find the index of the maximum element in the unsorted part
        max_index = arr.index(max(arr[:curr_size]))

        # Flip the prefix to bring the maximum element to the beginning
        flip(max_index)

        # Flip the entire prefix to bring the maximum element to its correct position
        flip(curr_size - 1)

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#pancake_sort(my_list)

#print("Sorted array (after Pancake Sort):", my_list)