import pytest
from sorted import InsertionSort

def test_empty_input():
    actual = InsertionSort([])
    expected = []
    assert actual == expected

def test_single_element():
    actual = InsertionSort([5])
    expected = [5]
    assert actual == expected

def test_two_element():
    actual = InsertionSort([5,10])
    expected = [5,10]
    assert actual == expected

def test_two_element2():
    actual = InsertionSort([50,10])
    expected = [10,50]
    assert actual == expected

def test_multiple_elements_in_random_order():
    actual = InsertionSort([9, 2, 5, 1, 7])
    expected = [1, 2, 5, 7, 9]
    assert actual == expected

def test_multiple_identical_elements():
    actual = InsertionSort([3, 2, 3, 1, 2])
    expected = [1, 2, 2, 3, 3]
    assert actual == expected