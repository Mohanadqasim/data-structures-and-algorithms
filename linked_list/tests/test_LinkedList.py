import pytest
from challenge.LinkedList import LinkedList
# from challenge.node import node

def test_str_empty_linked_list():
    actual =  str(LinkedList())
    expected = "list is empty"
    assert actual == expected

def test_insert():
    example = LinkedList()
    example.insert("A")
    actual = str(example)
    expected = " A ---> None"    
    assert actual == expected

def test_append():
    example = LinkedList()
    example.append("A")
    example.append("B")
    example.append("C")
    actual = str(example)
    expected = " A ---> B ---> C ---> None"    
    assert actual == expected

def test_insert_before():
    example = LinkedList()
    example.append("A")
    example.append("B")
    example.append("C")
    example.insert_before("B","X")
    actual = str(example)
    expected = " A ---> X ---> B ---> C ---> None"   
    assert actual == expected

def test_insert_after():
    example = LinkedList()
    example.append("A")
    example.append("B")
    example.append("C")
    example.insert_before("B","X")
    example.insert_after("B","Y")
    actual = str(example)
    expected = " A ---> X ---> B ---> Y ---> C ---> None"   
    assert actual == expected

# def test_included(example):
#     example = LinkedList()
#     example.append("A")
#     actual = str(example.include("A"))
#     expected = "True"
#     assert actual == expected

# def test_not_included(example):
#     example = LinkedList()
#     actual = str(example.include("X"))
#     expected = "False"
#     assert actual == expected

def test_delete():
    example = LinkedList()
    example.append("A")
    example.append("B")
    example.append("C")
    example.insert_before("B","X")
    example.insert_after("B","Y")
    example.delete("B")
    actual = str(example)
    expected = " A ---> X ---> Y ---> C ---> None"   
    assert actual == expected