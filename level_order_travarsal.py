class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def display_level(root, level):
    if not root:
        return
    if(level==1):
        print(root.data,end=" ")
    elif level > 1:
        display_level(root.left, level-1)
        display_level(root.right, level-1)


def height(node):
    if not node:
        return 0
    l = height(node.left)
    r = height(node.right)

    return max(l,r)+1

def display(root):
    h = height(root)
    for i in range(1,h+1):
        display_level(root,i)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

display(root)