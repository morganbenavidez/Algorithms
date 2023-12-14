def sentinel_linear_search(arr, target):
    n = len(arr)

    # Add a sentinel at the end of the array
    arr.append(target)

    i = 0
    while arr[i] != target:
        i += 1

    # Remove the sentinel
    arr.pop()

    if i < n:
        return i
    else:
        return -1

# Example usage:
"""
my_list = [3, 7, 4, 8, 6, 2, 1, 5]
target_value = 4

result = sentinel_linear_search(my_list, target_value)

if result != -1:
    print(f"Element {target_value} is present at index {result}.")
else:
    print(f"Element {target_value} is not present in the array.")
"""