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

def test_kthFromEnd_empty_list():
    example = LinkedList()
    actual = example.kthFromEnd(5)
    expected = "linked list is empty"   
    assert actual == expected


def test_kthFromEnd_greater_than_length():
    example = LinkedList()
    example.append("A")
    example.append("B")
    example.append("C")
    actual = example.kthFromEnd(5)
    expected = "invalid input"   
    assert actual == expected

def test_kthFromEnd_equals_length():
    example = LinkedList()
    example.append("A")
    example.append("B")
    example.append("C")
    actual = example.kthFromEnd(3)
    expected = "invalid input"   
    assert actual == expected

def test_kthFromEnd_negative_value():
    example = LinkedList()
    example.append("A")
    example.append("B")
    example.append("C")
    actual = example.kthFromEnd(-2)
    expected = "invalid input"   
    assert actual == expected

def test_kthFromEnd_length_equal_one():
    example = LinkedList()
    example.append("A")
    actual = example.kthFromEnd(5)
    expected = "A"   
    assert actual == expected

def test_kthFromEnd_Happy_Path():
    example = LinkedList()
    example.append("1")
    example.append("3")
    example.append("8")
    example.append("2")
    actual = example.kthFromEnd(0)
    expected = "2"   
    assert actual == expected

def test_kthFromEnd_Happy_Path2():
    example = LinkedList()
    example.append("1")
    example.append("3")
    example.append("8")
    example.append("2")
    actual = example.kthFromEnd(2)
    expected = "3"   
    assert actual == expected