'''
find height of tree 
check wheather root exist 
find length of left and right sub tree 
calculate current diameter
    curr_diameter = left + right +2 
find length of left diameter
find length of right diameter
return max(curr_dia,left_dia,right_dia) 

'''
class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None

def height(root):
    if root is None:
        return -1
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height,right_height)

def diameter(root):
    if root is None:
        return 0 
    left = height(root.left)
    right = height(root.right)
    curr_dia = left + right + 2 
    left_dia = diameter(root.left)
    right_dia = diameter(root.right)
    return max(curr_dia,left_dia,right_dia)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

print("Diameter of the tree is:",diameter(root))