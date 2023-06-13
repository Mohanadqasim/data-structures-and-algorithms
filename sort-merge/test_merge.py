import pytest
from sort_merg import merge_sort

def test_empty_input():
    actual = []
    merge_sort(actual)
    expected = []
    assert actual == expected

def test_single_element():
    actual = [5]
    merge_sort(actual)
    expected = [5]
    assert actual == expected

def test_two_element():
    actual = [5, 10]
    merge_sort(actual)
    expected = [5, 10]
    assert actual == expected

def test_two_element2():
    actual = [50, 10]
    merge_sort(actual)
    expected = [10, 50]
    assert actual == expected

def test_multiple_elements_in_random_order():
    actual = [9, 2, 5, 1, 7]
    merge_sort(actual)
    expected = [1, 2, 5, 7, 9]
    assert actual == expected

def test_multiple_identical_elements():
    actual = [3, 2, 3, 1, 2]
    merge_sort(actual)
    expected = [1, 2, 2, 3, 3]
    assert actual == expected
