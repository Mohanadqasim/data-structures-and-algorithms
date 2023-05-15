import pytest
from stack_queue_brackets import validate_brackets

def test_empty_string():
    string = ""
    expected = True
    actual = validate_brackets(string)
    assert expected == actual

def test_balanced_brackets():
    string = "(1 + [2 * {3 - 4}])"
    expected = True
    actual = validate_brackets(string)
    assert expected == actual

def test_unbalanced_brackets():
    string = "({[}])"
    expected = False
    actual = validate_brackets(string)
    assert expected == actual

def test_nested_brackets():
    string = "({[1 * (2 + 3)]})"
    expected = True
    actual = validate_brackets(string)
    assert expected == actual

def test_missing_closing_bracket():
    string = "({[1 + 2]"
    expected = False
    actual = validate_brackets(string)
    assert expected == actual

def test_extra_closing_bracket():
    string = "({[1 + 2]}))"
    expected = False
    actual = validate_brackets(string)
    assert expected == actual

def test_mixed_brackets():
    string = "({[1 + 2)]}"
    expected = False
    actual = validate_brackets(string)
    assert expected == actual
