# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None 
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)

# n1.next = n2 
# n2.next = n3 

# head = n1 
# temp = head
# while True:
#     if temp.next is None:
#         print(temp.data)
#         break
#     print(temp.data,end = "->")
#     temp = temp.next 
#     if temp is None:
#         break
# #inserting a node at beginning
# n4 = Node(100)
# n4.next = head 
# head = n4
# temp = head
# while True:
#     if temp.next is None:
#         print(temp.data)
#         break
#     print(temp.data,end = "->")
#     temp = temp.next 
#     if temp is None:
#         break
# n5 = Node(1)
# n5.next = head 
# head = n5 
# temp = head
# while True:
#     if temp.next is None:
#         print(temp.data)
#         break
#     print(temp.data,end = "->")
#     temp = temp.next 
#     if temp is None:
#         break
# #insert at random position 
# temp = head  
# pos = 1 
# while(pos<2):
#     temp = temp.next 
#     pos += 1 
# n6 = Node(300)
# n6.next = temp.next 
# temp.next = n6
# #printing ls
# temp = head
# while True:
#     if temp.next is None:
#         print(temp.data)
#         break
#     print(temp.data,end = "->")
#     temp = temp.next 
#     if temp is None:
#         break

# '''
# DELETION 
# '''
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None 
# def printing(head):
#     temp = head
#     while True:
#         if temp.next is None:
#             print(temp.data)
#             break
#         print(temp.data,end = "->")
#         temp = temp.next 
#         if temp is None:
#             break
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# head = n1
# n1.next = n2 
# n2.next = n3
# printing(head)

# def delbegin(head):
#     nextnode = head.next 
#     head.next = None 
#     head = nextnode
#     printing(head)
# # delbegin(head)

# def delend(head):
#     temp = head
#     while True:
#         if temp.next.next is None:
#             break
#         temp = temp.next 
#     temp.next = None 
#     printing(head)
# # delend(head)

# def delatpos(head,pos):
#     temp = head 
#     cur = 1 
#     while True:
#         if cur == pos-1:
#             break 
#         temp = temp.next 
#         cur += 1 
#     temp.next = temp.next.next 
#     printing(head)
# delatpos(head,)


'''
DOUBLE LS
'''
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
        self.prev = None 
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n1.next = n2 
n2.next = n3 
n3.prev = n2
n2.prev = n1
head = n1 
temp = head
def printrev(head):
    temp = head 
    #to traverse to last position
    while temp is not None:
        if temp.next is None:
            break 
        temp = temp.next 
    while temp is not None:
        if temp.prev is None:
            print(temp.data)
            break
        print(temp.data,end = "->")
        temp = temp.prev 
printrev(head)
def printing(head):
    temp = head  
    while temp is not None:
        if temp.next is None:
            print(temp.data)
            break
        print(temp.data,end = "->")
        temp = temp.next
printing(head)

def insertbeginning(head):
    newnode = Node(5)
    newnode.next = head 
    head.prev = newnode
    head = newnode
    printing(head)

def insertending(head):
    temp = head
    while True:
        if temp.next is None:
            break 
        temp = temp.next
    newnode = Node(50)
    temp.next = newnode 
    newnode.prev = temp 
    printing(head)
