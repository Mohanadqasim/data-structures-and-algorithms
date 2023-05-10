# Stack & Queue Animal Shelter

Author: Mohanad Qasim 

## Run the application:

pip install -r requirements.txt

python  main.py

pytest


## Whiteboard Process

![Alt text](./Untitled%20(5).jpg)

## Approach & Efficiency

> - Time --> O(1)
> - space -->O(n)

## Solution


```
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
```