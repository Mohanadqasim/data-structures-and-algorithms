# Validate bracket

Author: Mohanad Qasim 


## Run the application:

pip install -r requirements.txt

python  main.py

pytest


## Whiteboard Process



## Approach & Efficiency

> - Time --> O(N)
> - space -->O(N)

## Solution:
```
def validate_brackets(string):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    
    for i in string:
        if i in opening_brackets:
            stack.push(i)

        elif i in closing_brackets:
            if stack.is_empty():
                return False
            
            opening_bracket = stack.pop()
            if is_matching(opening_bracket, i) == False:
                return False
    
    return stack.is_empty()

def is_matching(open_bracket, close_bracket):
    if open_bracket == "(" and close_bracket == ")":
        return True
    
    elif open_bracket == "{" and close_bracket == "}":
        return True
    
    elif open_bracket == "[" and close_bracket == "]":
        return True
    
    else:
        return False
```