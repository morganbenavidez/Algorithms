def binary_search(arr, target, low, high):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def exponential_search(arr, target):
    n = len(arr)

    # Find the range where the target may be present
    if arr[0] == target:
        return 0
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # Perform binary search in the found range
    return binary_search(arr, target, i // 2, min(i, n - 1))

# Example usage:
"""
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5

result = exponential_search(sorted_array, target_value)

if result != -1:
    print(f"Element {target_value} is present at index {result}.")
else:
    print(f"Element {target_value} is not present in the array.")
"""