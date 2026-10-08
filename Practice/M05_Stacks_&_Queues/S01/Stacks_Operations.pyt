'''
Stack is linear DS which follows LIFO
Operations:
1.Push-Inserting elements
2.pop-Remove the data
3.peek - view the last element without removing 
4.is_empty - stack is empty or not 

Key points:
1.Overflow - Trying to insert in already filled stack 
2.Underflow - Trying to remove from empty satck 

Implementation:

1.Using Lists 
2.Using linked list
'''

#Stack using List

class Stack:
    def __init__(self):
        self.items = []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.items)
print(s.pop())
print(s.peek())
print(s.is_empty())
print(s.size())

#using Linked List 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Stack:
    def __init__(self):
        self.top = None 
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node 
    def pop(self):
        if not self.is_empty():
            val = self.top.data
            self.top = self.top.next 
            return val 
        return "Stack is empty"
    def peak(self):
        if not self.is_empty():
            return self.top.data
        return "Stack is emty"
    def is_empty(self):
        return self.top is None 
    def traverse(self):
        elements = []
        curr = self.top 
        while curr:



        