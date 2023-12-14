def cycle_sort(arr):
    writes = 0

    for cycleStart in range(len(arr) - 1):
        item = arr[cycleStart]

        # Find the position where we put the element
        pos = cycleStart
        for i in range(cycleStart + 1, len(arr)):
            if arr[i] < item:
                pos += 1

        # If the element is already in the correct position
        if pos == cycleStart:
            continue

        # Otherwise, put the element to the correct position
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        writes += 1

        # Rotate the rest of the cycle
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, len(arr)):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            writes += 1

    return writes

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#cycle_sort(my_list)

#print("Sorted array (after Cycle Sort):", my_list)