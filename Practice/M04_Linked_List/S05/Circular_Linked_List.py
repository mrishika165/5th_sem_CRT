'''
CIRCULAR LINKED LIST
the last node connects to the first node
Algorithm:
create node
insert data
connect nodes
traverse the nodes
'''
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n1.next = n2 
n2.next = n3 
n3.next = n4 
n4.next = n1 

def traverse():
    temp = n1
    while temp:
        print(temp.data,end = '->')
        temp = temp.next 
        if temp == n1:
            break 
    print("HEAD")
traverse()
    
    