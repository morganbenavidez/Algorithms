def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if the target is equal to the middle element
        if arr[mid] == target:
            return mid
        # If the target is smaller, search the left half
        elif arr[mid] > target:
            high = mid - 1
        # If the target is larger, search the right half
        else:
            low = mid + 1

    # If the target is not found, return -1
    return -1

# Example usage:
"""
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5

result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Element {target_value} is present at index {result}.")
else:
    print(f"Element {target_value} is not present in the array.")
"""