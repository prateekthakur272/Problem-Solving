class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def sorted_array_to_bst(arr):
    if(not arr):
        return None
    mid = (len(arr))//2
    root = Node(arr[mid])
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])
    return root

def display(node):
    if(not node):
        return None
    print(node.data)
    display(node.left)
    display(node.right)


arr = [1,2,3,4,5,6,7]
root = sorted_array_to_bst(arr)
display(root)