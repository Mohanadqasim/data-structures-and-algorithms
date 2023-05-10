import pytest
from animal_shelter.stack_queue_animal_shelter import AnimalShelter



def test_1 (list1):
    assert list1.dequeue("cat") == {"species" : "cat" , "name": "ash"}

def test_2 (list1):
    assert list1.dequeue("dog") == {"species" : "dog" , "name": "warwick"}

def test_3():
    AS = AnimalShelter()
    assert AS.dequeue("wolf") == None


@pytest.fixture
def list1():
    list1 = AnimalShelter()
    list1.enqueue({"species" : "cat" , "name": "ash"})
    list1.enqueue({"species" : "cat" , "name": "lux"})
    list1.enqueue({"species" : "cat" , "name": "neeko"})
    list1.enqueue({"species" : "dog" , "name": "warwick"})
    list1.enqueue({"species" : "dog" , "name": "garen"})
    list1.enqueue({"species" : "dog" , "name": "viego"})
    return list1