from queue_file import Queue

class AnimalShelter:
    def __init__(self):
        """this is the init for animal shelter where we assign dogs and cats' list"""
        self.cats = Queue()
        self.dogs = Queue()


    def enqueue(self,obj):
        """this is an enqueue method that takes species from class dog or cat"""
        if obj["species"] == "cat":
            self.cats.enqueue(obj) 
        if obj["species"] == "dog":
            self.dogs.enqueue(obj)   


    def dequeue(self,pref):
        """this is dequeue for any"""
        if pref != 'cat' and pref != 'dog':
            return None 
        if pref == 'cat' :
           return self.cats.dequeue()
        if pref == 'dog' :
           return self.dogs.dequeue()
        


ll = AnimalShelter()

ll.enqueue({"species" : "cat" , "name": "dddd"})
ll.enqueue({"species" : "cat" , "name": "eee"})
ll.enqueue({"species" : "cat" , "name": "fff"})
ll.enqueue({"species" : "dog" , "name": "xxx"})
ll.enqueue({"species" : "dog" , "name": "yyy"})
ll.enqueue({"species" : "dog" , "name": "gggg"})

print(ll.dequeue("cat"))
print(ll.dequeue("cat"))
ll.enqueue({"species" : "cat" , "name": "aaaa"})
print(ll.dequeue("cat"))

print(ll.dequeue("ss"))

print(ll.dequeue("dog"))
ll.enqueue({"species" : "dog" , "name": "zzzz"})
print(ll.dequeue("dog"))
print(ll.dequeue("dog"))