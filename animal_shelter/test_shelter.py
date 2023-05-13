import pytest
from stack_queue_animal_shelter import AnimalShelter



def test_animal_shelter_enqueue_cat():
    list = AnimalShelter()
    cat1 = {"species": "cat", "name": "Fluffy"}
    cat2 = {"species": "cat", "name": "Whiskers"}
    list.enqueue(cat1)
    list.enqueue(cat2)
    expected = "{'species': 'cat', 'name': 'Fluffy'} ---> {'species': 'cat', 'name': 'Whiskers'} ---> None"
    actual = list.__str__()
    assert actual == expected

def test_animal_shelter_enqueue_dog():
    list = AnimalShelter()
    dog1 = {"species": "dog", "name": "Buddy"}
    dog2 = {"species": "dog", "name": "Max"}
    list.enqueue(dog1)
    list.enqueue(dog2)
    expected = "{'species': 'dog', 'name': 'Buddy'} ---> {'species': 'dog', 'name': 'Max'} ---> None"
    actual = list.__str__()
    assert actual == expected

def test_animal_shelter_dequeue_cat():
    list = AnimalShelter()
    cat1 = {"species": "cat", "name": "Fluffy"}
    cat2 = {"species": "cat", "name": "Whiskers"}
    list.enqueue(cat1)
    list.enqueue(cat2)
    expected = "{'species': 'cat', 'name': 'Fluffy'}"
    actual = list.dequeue("cat")
    actual = str(actual)
    assert actual == expected

def test_animal_shelter_dequeue_dog():
    list = AnimalShelter()
    dog1 = {"species": "dog", "name": "Buddy"}
    dog2 = {"species": "dog", "name": "Max"}
    list.enqueue(dog1)
    list.enqueue(dog2)
    expected = "{'species': 'dog', 'name': 'Buddy'}"
    actual = list.dequeue("dog")
    actual = str(actual)
    assert actual == expected

def test_animal_shelter_dequeue_wrong():
    list = AnimalShelter()
    dog = {"species": "dog", "name": "Buddy"}
    cat = {"species": "cat", "name": "Fluffy"}
    list.enqueue(dog)
    list.enqueue(cat)
    expected = None
    actual = list.dequeue("wrone")
    assert actual == expected