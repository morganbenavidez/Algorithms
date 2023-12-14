def strand_sort(arr):
    result = []

    while arr:
        sublist = [arr.pop(0)]

        i = 0
        while i < len(arr):
            if arr[i] > sublist[-1]:
                sublist.append(arr.pop(i))
            else:
                i += 1

        result = merge(result, sublist)

    return result

def merge(list1, list2):
    result = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#sorted_array = strand_sort(my_list)

#print("Original array:", my_list)
#print("Sorted array (after Strand Sort):", sorted_array)