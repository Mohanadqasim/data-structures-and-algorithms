from node import Node

class Linked_List():
    def __init__(self):
        self.head = None

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
    
    def append(self,value):
        node = Node(value)
        
        if self.head is None:
            self.head=node
        
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    
    def insert_before(self,value,new):
        new_node = Node(new)
        current = self.head

        while (current):
            if current.value == value:
                new_node.next = self.head
                self.head = new_node
                return
                
            else:
                current = current.next
            

    def insert_after(self,value,new):
        new_node = Node(new)
        current = self.head

        while (current):
            if current.value == value:
                current.next = new_node
                return
            else:
                current = current.next