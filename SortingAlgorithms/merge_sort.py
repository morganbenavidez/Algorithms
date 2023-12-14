def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    i = j = k = 0

    # Compare and merge the elements from left_half and right_half
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Check for any remaining elements in left_half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Check for any remaining elements in right_half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#merge_sort(my_list)

#print("Sorted array (after Merge Sort):", my_list)