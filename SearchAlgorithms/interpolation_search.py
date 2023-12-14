def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Calculate the estimated position using interpolation formula
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        # If the target is found at the estimated position
        if arr[pos] == target:
            return pos
        # If the target is in the left half
        elif arr[pos] > target:
            high = pos - 1
        # If the target is in the right half
        else:
            low = pos + 1

    return -1

# Example usage:
"""
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5

result = interpolation_search(sorted_array, target_value)

if result != -1:
    print(f"Element {target_value} is present at index {result}.")
else:
    print(f"Element {target_value} is not present in the array.")
"""