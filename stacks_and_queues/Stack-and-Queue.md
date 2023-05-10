# Stacks and Queues

Author: Mohanad Qasim 


## Run the application:

pip install -r requirements.txt

python  main.py

pytest


## Whiteboard Process

![Alt text](./Untitled%20(2).jpg)

## Approach & Efficiency

> - Time --> O(1)
> - space -->O(1)
## Solution

### Queue

```
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
```

### Stack

```
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
```