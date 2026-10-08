'''
100 101 104 111 110
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
# def is_balanced(root):
#     if root is None:
#         return True 
#     Lh = height(root.left)
#     Rh = height(root.right)
#     if abs(Lh-Rh)<=1:
#         return True 
#     return False
# def check_height(root):
#     if root is None:
#         return 0 
#     left_height = check_height(root.left)
#     if left_height==-1:
#         return -1  
#     right_height = check_height(root.right)
#     if right_height==-1 :
#         return -1
#     return 1 + max(left_height,right_height)
# def is_balanced2(root):
#     return check_height!= -1
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of the tree is:",height(root))
# if is_balanced2(root):
#     print("the given Tree is balanced")
# else:
#     print("The tree is unbaalnced")
