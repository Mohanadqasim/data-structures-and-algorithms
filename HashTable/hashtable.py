
from LinkedList import LinkedList
class Hashtable:
    def __init__(self,size=3):
        self.max_size=size
        self.hash_map=[None]*size

    def hashing(self,key):
        summation=0
        for char in key:
            number = ord(char)
            summation+=number
        indx = (summation*599) % self.max_size
        return indx
    
    def set(self,key,value):
        hashed_key=self.hashing(key)

        if not self.hash_map[hashed_key]: #the bucket is empty
            self.hash_map[hashed_key]=[key,value]

        else: #the bucket already has an element or more
            if isinstance(self.hash_map[hashed_key], LinkedList):
                self.hash_map[hashed_key].add([key,value])
            else: # if the bucket contains one pair only
                chain = LinkedList()
                exsiting_pair = self.hash_map[hashed_key]
                new_pair = [key, value]
                self.hash_map[hashed_key] = chain
                chain.add(exsiting_pair)
                chain.add(new_pair)

    def get(self, key):
        hashed_key = self.hashing(key)

        if not self.hash_map[hashed_key]:  # the bucket is empty
            return None
        else:
            if isinstance(self.hash_map[hashed_key], LinkedList):
                chain = self.hash_map[hashed_key]
                node = chain.head
                while node:
                    if node.value[0] == key:
                        return node.value[1]
                    node = node.next
            else:  # if the bucket contains one pair only
                pair = self.hash_map[hashed_key]
                if pair[0] == key:
                    return pair[1]
        
        return None  
    
    def has(self, key):
        hashed_key = self.hashing(key)

        if not self.hash_map[hashed_key]:  # the bucket is empty
            return False
        else:
            if isinstance(self.hash_map[hashed_key], LinkedList):
                chain = self.hash_map[hashed_key]
                node = chain.head
                while node:
                    if node.value[0] == key:
                        return True
                    node = node.next
            else:  # if the bucket contains one pair only
                pair = self.hash_map[hashed_key]
                if pair[0] == key:
                    return True
        
        return False 
    
    def keys(self):
        keys = []

        for item in self.hash_map:
            if isinstance(item, LinkedList):
                chain = item
                node = chain.head
                while node:
                    keys.append(node.value[0])
                    node = node.next
            elif item:
                keys.append(item[0])
        
        return keys