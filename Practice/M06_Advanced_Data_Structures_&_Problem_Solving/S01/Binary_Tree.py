'''
Tree : non -linear DS
--> Non-linear : the data can be arranged in non-sequential 
--> The data is stored in nodes 
-->Node contain 3 parts 
    1.data part
    2.left part
    3.right part

    Representation of tree:
                  10  ----->level 0
                  / \
                20   30   --->level 1 
                / \    \
               40  50   60  --->level 2


Key Components :
1. Node-->Contains the data
2. Root-->Top node is called root node(10)
3. Edge-->Links or Connection btw nodes
4. Parent/child-->One node delivered from another (20-Parents node and 40-child node)
5.Sibilins--> two child nodes with a single parent node(20-Parent node and 40,50-child nodes)
6.Levels-->
7-->Height of the tree

'''
class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data , end = "->")
    inorder(root.right)  

def preorder(root):
    if root is None:
            return 
    print(root.data , end = "->")
    preorder(root.left)
    preorder(root.right)  

def postorder(root):
    if root is None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data , end = "->")

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
print("Inorder Traversal")
inorder(root)
print()
print("Preorder Traversal")
preorder(root)
print()
print("Postorder Traversal")
postorder(root)
print()
