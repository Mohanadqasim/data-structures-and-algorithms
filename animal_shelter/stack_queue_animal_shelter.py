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
        
    def __str__(self):
        output = ""
        if self.cats.front is None and self.dogs.front is None:
            output = "this queue is empty"
        else:
            current = self.cats.front
            while current is not None:
                output += f"{current.value} ---> "
                current = current.next
            current = self.dogs.front
            while current is not None:
                output += f"{current.value} ---> "
                current = current.next
            output += "None"
        return output