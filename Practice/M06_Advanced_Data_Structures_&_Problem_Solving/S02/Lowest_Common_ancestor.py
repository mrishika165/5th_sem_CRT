class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None 
#Tree Structure
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def LCA(root,p,q):
    if root is None:
        return None 
    if root.data == p or root.data == q:
        return root.data
    left = LCA(root.left,p,q)
    right = LCA(root.right,p,q)
    if left and right:
        return root.data
    if left is not None:
        return left
    else:
        return right

print(LCA(root,1,2))
        