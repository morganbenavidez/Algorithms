class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    return root

def in_order_traversal(root, result):
    if root:
        in_order_traversal(root.left, result)
        result.append(root.key)
        in_order_traversal(root.right, result)

def tree_sort(arr):
    root = None

    for element in arr:
        root = insert(root, element)

    result = []
    in_order_traversal(root, result)
    return result

# Example usage:
#my_list = [3, 7, 4, 8, 6, 2, 1, 5]
#sorted_array = tree_sort(my_list)

#print("Original array:", my_list)
#print("Sorted array (after Tree Sort):", sorted_array)