from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,value):
        node = Node(value)
        
        if self.head is None:
            self.head=node
        
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def __str__(self):
        output = ""
        
        if self.head == None:
            output = "list is empty"
        
        else:
            current = self.head
            while (current):
                output = output + f' {current.value} --->'
                current = current.next
            output += " None"
        return output
    
    def include(self, key):
        current = self.head
        while (current):
            if current.value == key:
                return True
            else:
                current = current.next
        return False

