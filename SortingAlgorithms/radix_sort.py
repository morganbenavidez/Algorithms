def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Do counting sort for every digit, starting from the least significant digit (LSD)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit at the current place value
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Update count to store the position of each digit in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array using the count array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

# Example usage:
#my_list = [170, 45, 75, 90, 802, 24, 2, 66]
#radix_sort(my_list)

#print("Sorted array (after Radix Sort):", my_list)