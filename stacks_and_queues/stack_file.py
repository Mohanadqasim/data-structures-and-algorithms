# from Stacks_and_queues.node import Node
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.size=0

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top=node
        self.size+=1

    def pop(self):
        if self.top == None:
            return("stack is empty")
        else:
            temp = self.top
            self.top = self.top.next
            self.size-=1
            return temp.value
    
    def peek(self):
        if self.top:
            return (self.top.value)
        else:
            return ("stack is empty")
        
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def __str__(self):
        output = ""
        if self.top is None:
            output = "stack is empty"
        else:
            current = self.top
            while(current):
                output += ('{} ---> '.format(current.value))
                current = current.next
            
            output += " None"
        return output