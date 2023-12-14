def pigeonhole_sort(arr):
    if not arr:
        return arr

    # Find the minimum and maximum values in the array
    min_val, max_val = min(arr), max(arr)
    range_size = max_val - min_val + 1

    # Create pigeonholes (buckets)
    pigeonholes = [0] * range_size

    # Distribute elements into pigeonholes
    for num in arr:
        pigeonholes[num - min_val] += 1

    # Reconstruct the sorted array based on pigeonholes
    sorted_arr = []
    for i in range(range_size):
        sorted_arr.extend([i + min_val] * pigeonholes[i])

    return sorted_arr

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#sorted_array = pigeonhole_sort(my_list)

#print("Original array:", my_list)
#print("Sorted array (after Pigeonhole Sort):", sorted_array)