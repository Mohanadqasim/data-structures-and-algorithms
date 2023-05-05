import pytest
from Stacks_and_queues.Node import Node
from Stacks_and_queues.Queue import Queue
from Stacks_and_queues.Stack import Stack

def test_empty_queue():
    queue = Queue()
    expected = "this queue is empty"
    actual = str(queue)
    assert expected == actual

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected="1 ---> 2 ---> 3 --->  None"
    actual = str(queue)
    assert expected == actual

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    expected="2 ---> 3 --->  None"
    actual = str(queue)
    assert expected == actual

def test_dequeue_empty():
    queue = Queue()
    queue.dequeue()
    expected="this queue is empty"
    actual = str(queue)
    assert expected == actual

def test_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    excepted="1"
    actual = Queue.peek(queue)
    assert excepted == actual
################################stack################################

def test_empty_stack():
    stack = Stack()
    expected = "stack is empty"
    actual = str(stack)
    assert expected == actual

def test_stack_push():
    stack=Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    excepted = "c ---> b ---> a --->  None"
    actual = str(stack)
    assert excepted == actual

def test_stack_pop_empty():
    stack=Stack()
    stack.pop()
    excepted = "stack is empty"
    actual = str(stack)
    assert excepted == actual

def test_stack_pop():
    stack=Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    stack.pop()
    excepted = "b ---> a --->  None"
    actual = str(stack)
    assert excepted == actual

def test_stack_peek_empty():
    stack=Stack()
    excepted = "stack is empty"
    actual = stack.peek()
    assert excepted == actual

def test_stack_peek():
    stack=Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    excepted = "c"
    actual = stack.peek()
    assert excepted == actual

def test_stack_get_size_empty():
    stack=Stack()
    excepted = "0"
    actual = stack.get_size()
    assert excepted == actual

def test_stack_get_size():
    stack=Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    excepted = "3"
    actual = stack.get_size()
    assert excepted == actual

def test_stack_get_is_empty():
    stack=Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    excepted = "False"
    actual = stack.is_empty()
    assert excepted == actual