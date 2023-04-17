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

def test_append():
    example = LinkedList()
    example.append("B")
    example.append("C")
    actual = str(example)
    expected = "A ---> B ---> C ---> None"    
    assert actual == expected

def test_insert_before():
    example = LinkedList()
    example.insert_before("B","X")
    actual = str(example)
    expected = "A ---> X ---> B ---> C ---> None"   
    assert actual == expected

def test_insert_after():
    example = LinkedList()
    example.insert_after("B","Y")
    actual = str(example)
    expected = "A ---> X ---> B ---> Y ---> C ---> None"   
    assert actual == expected

def test_included(example):
    actual = str(example.includes("A"))
    expected = "True"
    assert actual == expected

def test_not_included(example):
    actual = str(example.includes("X"))
    expected = "False"
    assert actual == expected

def test_delete():
    example = LinkedList()
    example.delete("B")
    actual = str(example)
    expected = "A ---> X ---> Y ---> C ---> None"   
    assert actual == expected