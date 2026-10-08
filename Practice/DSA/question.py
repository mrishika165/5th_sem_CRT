class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
def printing(head):
    temp = head
    while True:
        if temp.next is None:
            print(temp.data)
            break
        print(temp.data,end = "->")
        temp = temp.next 
        if temp is None:
            break
n1 = Node(1)
head = n1 
temp = head 
printing(head)
#insertion at beginning
n2 = Node(30)
n2.next = head 
head = n2 
printing(head)  
#insertion at end
n3 = Node(45)
temp = head 
#traversing
while temp.next is not None:
    temp = temp.next
temp.next = n3 
printing(head)
#insertion at position
n4 = Node(35)
temp = head 
pos = 1
while(pos<3):
    temp = temp.next 
    pos += 1 
n4.next = temp.next 
temp.next = n4 
printing(head)
#INSERT 45 AFTER 35
n5 = Node(45)
temp = head 
while temp.data != 35:
    temp = temp.next 
temp.next = n5 
printing(head)
