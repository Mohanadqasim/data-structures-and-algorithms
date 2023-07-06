# Tree Intersection

## Problem Domain
Write a function which is called tree_intersection, the function has to find the intersection of values between two binary trees. Given two binary trees, the function should identify and return a set of values that are present in both trees.

## Big O Notation
- Time Complexity: O(n)
- Space Complexity: O(m+k)

n:the maximum number of nodes

m:the number of unique values in BT1

k:the number of common values between BT1 and BT2


## Code 
```
def tree_intersection(BT1, BT2):
    if BT1 is None or BT2 is None:
        return set()

    intersection_set = set()
    hashtable = Hashtable()

    # Create a Hashtable and add values from BT1
    first_tree = Binary_tree()
    first_tree_values = first_tree.in_order(BT1)
    for value in first_tree_values:
        hashtable.set(str(value), True)  # Convert value to string

    # Check for intersection with values from BT2
    second_tree = Binary_tree()
    second_tree_values = second_tree.in_order(BT2)
    for value in second_tree_values:
        if hashtable.has(str(value)):  # Convert value to string
            intersection_set.add(value)

    return intersection_set
```