def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)

    # Calculate the range of each bucket
    bucket_range = (max_val - min_val) / (len(arr) - 1)

    # Create buckets
    buckets = [[] for _ in range(len(arr))]

    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    # Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # Concatenate the sorted buckets
    sorted_arr = [num for bucket in buckets for num in bucket]

    return sorted_arr

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#sorted_array = bucket_sort(my_list)

#print("Original array:", my_list)
#print("Sorted array (after Bucket Sort):", sorted_array)