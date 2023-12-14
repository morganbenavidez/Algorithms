def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
"""
my_list = [3, 7, 4, 8, 6, 2, 1, 5]
target_value = 4

result = linear_search(my_list, target_value)

if result != -1:
    print(f"Element {target_value} is present at index {result}.")
else:
    print(f"Element {target_value} is not present in the array.")
"""