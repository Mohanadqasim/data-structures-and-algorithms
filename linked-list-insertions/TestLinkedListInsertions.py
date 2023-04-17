import pytest
from LinkedListInsertions import Linked_List

def test_str_empty_linked_list():
    actual =  str(Linked_List())
    expected = "list is empty"
    assert actual == expected

def test_append():
    example = Linked_List()
    example.append("A")
    actual = str(example)
    expected = "A ---> None"    
    assert actual == expected

@pytest.fixture
def example():
    example = Linked_List()
    example.append("A")
    example.append("B")
    example.append("C")
    return example
