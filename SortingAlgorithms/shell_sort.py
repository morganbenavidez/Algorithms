def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        gap //= 2

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#shell_sort(my_list)

#print("Sorted array (after Shell Sort):", my_list)