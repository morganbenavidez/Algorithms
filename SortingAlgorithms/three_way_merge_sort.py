def three_way_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr))]

    while stack:
        start, end = stack.pop()

        if end - start > 1:
            mid1 = start + (end - start) // 3
            mid2 = start + 2 * (end - start) // 3

            stack.append((mid2, end))
            stack.append((mid1, mid2))
            stack.append((start, mid1))
        else:
            continue

        # Merge the sorted parts
        result = merge_three_parts(arr[start:mid1], arr[mid1:mid2], arr[mid2:end])
        arr[start:end] = result

    return arr

def merge_three_parts(part1, part2, part3):
    result = []
    i = j = k = 0

    while i < len(part1) or j < len(part2) or k < len(part3):
        val1 = part1[i] if i < len(part1) else float('inf')
        val2 = part2[j] if j < len(part2) else float('inf')
        val3 = part3[k] if k < len(part3) else float('inf')

        if val1 <= val2 and val1 <= val3:
            result.append(part1[i])
            i += 1
        elif val2 <= val1 and val2 <= val3:
            result.append(part2[j])
            j += 1
        else:
            result.append(part3[k])
            k += 1

    return result

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#sorted_array = three_way_merge_sort(my_list.copy())

#print("Original array:", my_list)
#print("Sorted array (after Three-Way Merge Sort):", sorted_array)