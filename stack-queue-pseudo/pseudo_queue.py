# from node import Node
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Pseudo_queue:
    def __init__(self):
        self.front=None
        self.rear=None

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

    def enqueue(self,value):
        node = Node(value)
        #if the queue is empty:
        if not self.front:
            self.front=node
            self.rear=node
        #otherwise
        else:
            node.next = self.front
            self.front = node

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
        while temp.next != self.rear:
            temp=temp.next
        value=self.rear.value
        self.rear=temp
        self.rear.next=None
        return value

    def peek(self):
        #if the queue is empty:
        if self.front is None:
            return ("this queue is empty")
        
        #otherwise:
        return self.front.value