class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    l = 0
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
        self.l+=1
        node = Node(value)
        node.next = self.head
        self.head = node
        


    def append(self,value):
        self.l+=1
        node = Node(value)
        if self.head is None:
            self.head=node        
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node


    def insert_before(self,value,new):
        self.l+=1
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
        self.l+=1
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
        self.l-=1
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
    
    def kthFromEnd(self,k):
        length = self.l
        if self.head is None:
            return "linked list is empty"
        elif length == 1:
            return self.head.value
        elif k > length:
            return "invalid input"
        elif k == length:
            return "invalid input"
        elif k < 0:
            return "invalid input"
        else:
            index=length-1
            node_index=index-k
            temp=self.head
            temp_index=0
            while temp:
                if temp_index == node_index:
                    return temp.value
                else:
                    temp_index+=1
                    temp=temp.next
                    

def zip_lists(list1, list2):
    if not list1.head or not list2.head:
        return list1 if list1.head else list2

    new_list = LinkedList()
    current1 = list1.head
    current2 = list2.head
    new_list.head = current1

    while current1 and current2:
        temp1 = current1.next
        temp2 = current2.next

        current1.next = current2
        current2.next = temp1

        current1 = temp1
        current2 = temp2
        
    if current2:
        while current2:
            new_list.append(current2.value)
            current2=current2.next

    return new_list


