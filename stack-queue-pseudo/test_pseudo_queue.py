from pseudo_queue import Pseudo_queue
import pytest

def test_empty_queue():
    queue = Pseudo_queue()
    expected = "this queue is empty"
    actual = str(queue)
    assert expected == actual

def test_enqueue():
    queue = Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected="3 ---> 2 ---> 1 --->  None"
    actual = str(queue)
    assert expected == actual

def test_dequeue_empty():
    queue = Pseudo_queue()
    queue.dequeue()
    expected="this queue is empty"
    actual = str(queue)
    assert expected == actual

def test_dequeue():
    queue = Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    expected="3 ---> 2 --->  None"
    actual = str(queue)
    assert expected == actual

def test_peek():
    queue = Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    excepted=3
    actual = Pseudo_queue.peek(queue)
    assert excepted == actual