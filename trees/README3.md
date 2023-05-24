# Breadth First

Author: Mohanad Qasim 


## Run the application:

pip install -r requirements.txt

python  main.py

pytest


## Whiteboard Process

![Alt text](./Untitled%20(10).jpg)

## Approach & Efficiency
> - Time --> O(N)
> - space -->O(N)

## Solution
```
def breadth_first(root):
    result_list = []
    if root is None:
        return result_list

    queue = [root]
    index = 0

    while index < len(queue):
        node = queue[index]
        result_list.append(node.value)
        index += 1

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return result_list

```