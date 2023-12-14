import random

def bingo_sort(arr):
    n = len(arr)
    
    # Keep sorting until the list is sorted
    while not is_sorted(arr):
        # Randomly swap adjacent elements
        i = random.randint(0, n-2)
        arr[i], arr[i+1] = arr[i+1], arr[i]

def is_sorted(arr):
    # Check if the list is sorted
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

# Example usage:
#my_list = [64, 25, 12, 22, 11]
#bingo_sort(my_list)

#print("Sorted array:", my_list)