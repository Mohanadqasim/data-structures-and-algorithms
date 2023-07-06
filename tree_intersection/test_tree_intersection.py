import pytest
from Trees import Binary_tree
from Node import Node
from tree_intersection import tree_intersection

@pytest.fixture
def test_BST():
    tree1 = Binary_tree()
    node1 = Node(150)
    node2 = Node(100)
    node3 = Node(75)
    node4 = Node(125)
    node5 = Node(160)
    node6 = Node(175)
    node7 = Node(250)
    node8 = Node(200)
    node9 = Node(300)
    node10 = Node(350)
    node11 = Node(450)

    tree1.root = node1
    node1.left = node2
    node1.right = node7
    node2.left = node3
    node2.right = node5
    node5.left = node4
    node5.right = node6
    node7.left = node8
    node7.right = node10
    node10.left = node9
    node10.right = node11

    return tree1.root


@pytest.fixture
def test_BST2():
    tree2 = Binary_tree()
    node1 = Node(200)
    node2 = Node(300)
    node3 = Node(175)
    node4 = Node(125)
    node5 = Node(250)
    node6 = Node(400)
    node7 = Node(150)
    node8 = Node(350)
    node9 = Node(600)
    node10 = Node(450)
    node11 = Node(500)

    tree2.root = node1
    node1.left = node2
    node1.right = node7
    node2.left = node3
    node2.right = node5
    node5.left = node4
    node5.right = node6
    node7.left = node8
    node7.right = node10
    node10.left = node9
    node10.right = node11

    return tree2.root


def test_tree_intersection_one(test_BST, test_BST2):
    expected = {125, 150, 175, 200, 250, 300, 350, 450}
    assert tree_intersection(test_BST, test_BST2) == expected


def test_tree_intersection_two():
    first_tree = Binary_tree()
    second_tree = Binary_tree()
    expected = set()
    assert tree_intersection(first_tree.root, second_tree.root) == expected


def test_tree_intersection_three():
    first_tree = Binary_tree()
    second_tree = Binary_tree()
    node1 = Node(50)
    node2 = Node(25)
    node3 = Node(75)
    node4 = Node(12)
    node5 = Node(40)
    node6 = Node(60)
    node7 = Node(90)

    first_tree.root = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    expected = set()
    assert tree_intersection(first_tree.root, second_tree.root) == expected


def test_tree_intersection_four():
    first_tree = Binary_tree()
    second_tree = Binary_tree()
    node1 = Node(50)
    node2 = Node(25)
    node3 = Node(75)
    node4 = Node(12)
    node5 = Node(40)
    node6 = Node(60)
    node7 = Node(90)

    first_tree.root = node1
    node1.left = node2
    node1.right =node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    node8 = Node(25)
    node9 = Node(60)
    node10 = Node(90)

    second_tree.root = node8
    node8.left = node9
    node8.right = node10

    expected = {25, 60, 90}
    assert tree_intersection(first_tree.root, second_tree.root) == expected
