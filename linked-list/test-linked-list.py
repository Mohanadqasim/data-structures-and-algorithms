import pytest
from LinkedList import LinkedList

def test_str_empty_linked_list():
    actual =  str(LinkedList())
    expected = "list is empty"
    assert actual == expected

def test_insert():
    example = LinkedList()
    example.insert("A")
    actual = str(example)
    expected = "A ---> None"    
    assert actual == expected

def test_included(example):
    actual = str(example.includes("A"))
    expected = "True"
    assert actual == expected

def test_not_included(example):
    actual = str(example.includes("X"))
    expected = "False"
    assert actual == expected

@pytest.fixture
def example():
    example = LinkedList()
    example.insert("A")
    return example