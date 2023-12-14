def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, left, mid, right):
    len_left = mid - left + 1
    len_right = right - mid

    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len_left and j < len_right:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right_part[j]
        j += 1
        k += 1

def tim_sort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n-1))

            if mid < right:
                merge(arr, left, mid, right)

        size *= 2

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#tim_sort(my_list)

#print("Original array:", my_list)
#print("Sorted array (after Tim Sort):", my_list)