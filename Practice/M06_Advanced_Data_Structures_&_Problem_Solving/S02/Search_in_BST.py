class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.right = Node(7)
root.right.left = Node(15)

def search(root,val):
    if root is None:
        return False 
    if root.data == val:
        return True
    elif val < root.data:
        return search(root.left,val)
    else:
        return search(root.right,val)
    return False
print(search(root,5))
print(search(root,30))