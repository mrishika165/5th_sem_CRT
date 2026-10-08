'''
Circular Queue:
the l;ast rear part is connected go front part
there is no wastage of empty spaces 

Implementation:
1.Enqueue
2.dequeue
3.is_empty:
4.is_full
'''
class CircularQueue:
    def __init__(self,capacity):
        self.capacity = capacity 
        self.front = 0 
        self.rear = -1
        self.size = 0 
    def is_empty(self):
        return self.size == 0 
    def is_full(self):
        return self.size == self.capacity
    def enqueue(self,data):
        if self.is_full():
            return "Queue is full"
        self.rear = (self.rear+1)%self.capacity
        self.queue[self.rear] = data 
        self.size += 1 
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        self.front = (self.front+1)%self.capacity
        
    