import pytest
from ArrayBinarySearch import binary_search

def test_binary_searh_no_elements(arr,n):
    actual = binary_search([],1)
    expected = -1
    assert actual == expected

def test_binary_searh_no_element(arr,n):
    actual = binary_search([1, 2, 3, 4, 5],6)
    expected = -1
    assert actual == expected

def test_binary_searh_one_elements(arr,n):
    actual = binary_search([5],5)
    expected = 0
    assert actual == expected

def test_binary_searh_basic_input(arr,n):
    actual = binary_search([1, 2, 3, 4, 5],3)
    expected = 2
    assert actual == expected

def test_binary_searh_duplicate_elements(arr,n):
    actual = binary_search([1, 2, 2, 3, 4, 4, 5],2)
    expected = 1
    assert actual == expected