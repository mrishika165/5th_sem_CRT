'''
Queues is linear DS which follows FIFO 

operations:
1.Enqueue - insert the data 
2.dequeue - removing the element 
3.peak: returns starting of the node without removing 
4.is_empty : checks the queue is empty or not

key points:'
1.front - starting of queue 
2.rear - ending of queue 

Implementation:
1.using List 
2.Using Linked List

'''
#using List 

# class Queue:
#     def __init__(self):
#         self.items = []
#     def enqueue(self,data):
#         self.items.append(data)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         return "Stack is empty"
#     def peak(self):
#         if not self.is_empty():
#             return self.items[0]
#         return "Stack is empty"
#     def is_empty(self):
#         return len(self.items)==0
#     def size(self):
#         return len(self.items)
# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# print(q.items)
# print(q.dequeue())
# print(q.peak())
# print(q.is_empty())
# print(q.size())


#using linked list 
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None 
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.is_empty():
            return " Queue is empty"
        val = self.front.data = 10 
        self.front = self.front.next 
        if self.front is None:
            self.rear = None 
        return val
    def display(self):
        if self.is_empty():
            return " Queue is empty"
        res = []
        curr = self.front 
        while curr:
            res.append(curr.data)
            curr = curr.next 
        return res 
    

