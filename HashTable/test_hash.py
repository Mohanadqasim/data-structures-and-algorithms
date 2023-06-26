import pytest

from hashtable import Hashtable

def test_hashtable():
    hash_table = Hashtable()
    expected = 3
    actual = len(hash_table.hash_map)
    assert expected == actual

def test_set_new_element():
    hash_table = Hashtable()
    hash_table.set("A", 30)
    expected = 30
    actual = hash_table.get("A")
    assert expected == actual

def test_get_existing_key():
    hash_table = Hashtable()
    hash_table.set("A", 30)
    expected = 30
    actual = hash_table.get("A")
    assert expected == actual

def test_get_nonexistent_key():
    hash_table = Hashtable()
    expected = None
    actual = hash_table.get("B")
    assert expected == actual

def test_keys(test_case):
    expected = ["A"]
    assert test_case.keys() == expected

def test_collision():
    hash_table = Hashtable(size=1)
    hash_table.set("A", 30)
    hash_table.set("B", 40)
    expected = 40
    actual = hash_table.get("B")
    assert expected == actual

def test_retrieve_collision_value():
    hash_table = Hashtable(size=1)
    hash_table.set("A", 30)
    hash_table.set("B", 40)
    expected = 30
    actual = hash_table.get("A")
    assert expected == actual

def test_hashing():
    hash_table = Hashtable(size=10)
    key = "A"
    expected = 5
    actual = hash_table.hashing(key)
    assert expected == actual

@pytest.fixture
def test_case():
    hash_table = Hashtable()
    hash_table.set("A", 30)
    return hash_table
