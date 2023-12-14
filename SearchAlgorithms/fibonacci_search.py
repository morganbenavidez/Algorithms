def min_fibonacci_numbers(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    fib.pop()  # Remove the last Fibonacci number that is greater than or equal to n
    return fib

def fibonacci_search(arr, target):
    n = len(arr)
    fib = min_fibonacci_numbers(n)

    offset = 0
    while fib:
        i = min(offset + fib[-1], n - 1)

        if arr[i] == target:
            return i
        elif arr[i] < target:
            fib.pop()
            offset = i
        else:
            fib.pop()

    return -1

# Example usage:
"""
sorted_array = [1, 2, 3, 4, 7, 5, 7, 8, 9]
target_value = 5

result = fibonacci_search(sorted_array, target_value)

if result != -1:
    print(f"Element {target_value} is present at index {result}.")
else:
    print(f"Element {target_value} is not present in the array.")
"""