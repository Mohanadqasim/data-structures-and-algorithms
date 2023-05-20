# Binary Trees

Author: Mohanad Qasim 


## Run the application:

pip install -r requirements.txt

python  main.py

pytest


## Whiteboard Process

![Alt text](./Untitled%20(8).jpg)

## Approach & Efficiency

Binary_tree:
> - Time --> O(N)
> - space -->O(N)

Binary_search_tree:

Avg Cases:
> - Time --> O(log(N))
> - space -->O(log(N))

Worst cases:
> - Time --> O(N)
> - space -->O(N)

## Solution

```
class Binary_tree:
    def __init__(self):
        self.root = None
        self.result_list = []
    
    def pre_order(self, root):
        if root is not None:
            self.result_list.append(root.value)  
        if root.left is not None:
            self.pre_order(root.left)
        if root.right is not None:
            self.pre_order(root.right)
        return self.result_list
    
    def in_order(self, root):
        if root.left is not None:
            self.in_order(root.left)
        if root is not None:
            self.result_list.append(root.value)  
        if root.right is not None:
            self.in_order(root.right)
        return self.result_list
    
    def post_order(self, root):
        if root.left is not None:
            self.post_order(root.left)
        if root.right is not None:
            self.post_order(root.right)
        if root is not None:
            self.result_list.append(root.value)  
        return self.result_list

class Binary_Search_Tree(Binary_tree):
    def __init__(self):
        super().__init__()

    def add(self, root, value):
        if root is None:
            self.root = Node(value)
            return

        if root.value > value:
            if root.left is None:
                root.left = Node(value)
            else:
                self.add(root.left, value)

        elif root.value < value:
            if root.right is None:
                root.right = Node(value)
            else:
                self.add(root.right, value)

    def contain(self, root, value):
        if root is None:
            return False

        if root.value == value:
            return True

        if root.value > value:
            return self.contain(root.left, value)

        if root.value < value:
            return self.contain(root.right, value)

        return False
```