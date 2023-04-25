class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
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

    def insert(self, value):

        node = Node(value)

        node.next = self.head
        self.head = node


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

        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return
    
        current = self.head.next
        prev = self.head
    
        while current is not None:
            if current.value == value:
                prev.next = new_node
                new_node.next = current
                return
            prev = current
            current = current.next

    def insert_after(self,value,new):
        node = Node(new)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while(current):
                if current.value == value:
                    node.next = current.next
                    current.next = node
                    return
                else:
                    current = current.next
    
    def include(self, key):
        current = self.head
        while (current):
            if current.value == key:
                return True
            else:
                current = current.next
        return False
    
    def delete(self, value):
        if self.head is None:
            return
    
        if self.head.value == value:
            self.head = self.head.next
            return
    
        current = self.head.next
        prev = self.head
    
        while current is not None:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next

