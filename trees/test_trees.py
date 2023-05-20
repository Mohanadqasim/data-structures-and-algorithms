from Trees import Binary_tree, Binary_Search_Tree
from Node import Node
import pytest

@pytest.fixture
def empty_tree():
    binary_tree = Binary_tree()
    return binary_tree

@pytest.fixture
def single_node_tree():
    binary_tree = Binary_tree()
    binary_tree.root = Node(1)
    return binary_tree

def test_empty_tree(empty_tree):
    assert empty_tree.root is None

def test_single_node_tree(single_node_tree):
    assert single_node_tree.root.value == 1
    assert single_node_tree.root.left is None
    assert single_node_tree.root.right is None

def test_add_left_and_right_child():
    bst = Binary_Search_Tree()
    values = [5, 3, 7, 2, 4, 6, 8]

    for value in values:
        bst.add(bst.root, value)

    assert bst.root.left.value == 3
    assert bst.root.right.value == 7
    assert bst.root.left.left.value == 2
    assert bst.root.left.right.value == 4
    assert bst.root.right.left.value == 6
    assert bst.root.right.right.value == 8

def test_traversal_pre_order():
    bst = Binary_Search_Tree()
    values = [10, 5, 15, 3, 7, 12, 17]

    for value in values:
        bst.add(bst.root, value)

    expected_pre_order = [10, 5, 3, 7, 15, 12, 17]
    actual_pre_order = bst.pre_order(bst.root)
    assert actual_pre_order == expected_pre_order

def test_traversal_in_order():
    bst = Binary_Search_Tree()
    values = [10, 5, 15, 3, 7, 12, 17]

    for value in values:
        bst.add(bst.root, value)

    expected_in_order = [3, 5, 7, 10, 12, 15, 17]
    actual_in_order = bst.in_order(bst.root)
    assert actual_in_order == expected_in_order

def test_traversal_post_order():
    bst = Binary_Search_Tree()
    values = [10, 5, 15, 3, 7, 12, 17]

    for value in values:
        bst.add(bst.root, value)

    expected_post_order = [3, 7, 5, 12, 17, 15, 10]
    actual_post_order = bst.post_order(bst.root)
    assert actual_post_order == expected_post_order

def test_contain_empty_tree():
    bst = Binary_Search_Tree()
    expected = False
    actual = bst.contain(bst.root, 5)
    assert expected == actual

def test_contain_non_existing_node():
    bst = Binary_Search_Tree()
    values = [10, 5, 15, 3, 7, 12, 17]

    for value in values:
        bst.add(bst.root, value)

    expected = False
    actual = bst.contain(bst.root, 9)
    assert expected == actual

def test_contain_non_existing_node():
    bst = Binary_Search_Tree()
    values = [10, 5, 15, 3, 7, 12, 17]

    for value in values:
        bst.add(bst.root, value)
        
    expected = True
    actual = bst.contain(bst.root, 12)
    assert expected == actual