from Node import Node

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    


    def enqueue(self,value):
        node=Node(value)
        #if the queue is empty:
        if not self.front:
            self.front=node
            self.rear=node
            
        #otherwise:
        else:
            self.rear.next=node
            self.rear=node



    def dequeue(self):
        #if the queue is empty:
        if self.front is None:
            return ("this queue is empty")
        
        #if the queue has only one element:
        if self.front == self.rear:
            self.rear=None
            self.front=None
            
        #if the queue has more than one value:
        temp=self.front
        self.front=self.front.next
        temp.next=None
        return temp.value
    


    def peek(self):
        #if the queue is empty:
        if self.front is None:
            return ("this queue is empty")
        
        #otherwise:
        return self.front.value
    


    def is_empty(self):
        return self.front== None
    


    def __str__(self):
        output = ""
        if self.front is None:
            output = "this queue is empty"
        else:
            current = self.front
            while(current):
                output += '{} ---> '.format(current.value)
                current = current.next
            
            output += " None"
        return output  