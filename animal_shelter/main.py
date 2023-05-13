from stack_queue_animal_shelter import AnimalShelter
if __name__ == '__main__':
    shelter = AnimalShelter()


    shelter.enqueue({"species": "cat", "name": "Fluffy"})
    shelter.enqueue({"species": "dog", "name": "Buddy"})
    shelter.enqueue({"species": "dog", "name": "Max"})
    shelter.enqueue({"species": "cat", "name": "Whiskers"})


    print(shelter)
    print(shelter.dequeue("cat"))
    print(shelter)
    print(shelter.dequeue("dog"))
    print(shelter)
    print(shelter.dequeue("wrong"))