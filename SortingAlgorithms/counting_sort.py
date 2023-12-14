def counting_sort(arr):
    if not arr:
        return arr

    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)

    # Create a count array to store the occurrences of each element
    count = [0] * (max_val - min_val + 1)

    # Count the occurrences of each element in the array
    for num in arr:
        count[num - min_val] += 1

    # Reconstruct the sorted array based on the count array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#sorted_array = counting_sort(my_list)

#print("Original array:", my_list)
#print("Sorted array (after Counting Sort):", sorted_array)