# Max Value

Author: Mohanad Qasim 


## Run the application:

pip install -r requirements.txt

python  main.py

pytest


## Whiteboard Process

![Alt text](./Untitled%20(9).jpg)

## Approach & Efficiency
> - Time --> O(N)
> - space -->O(log(N))

## Solution
```
def maximum_value(self):
        if self.root is None:
            return None
        if self.max_value is None:
            self.max_value=self.root.value
        def find_max (root):
              if root.left: find_max(root.left)
              if root.right: find_max(root.right)
              if root.value > self.max_value:
                    self.max_value = root.value      
        find_max(self.root)
        return self.max_value
```