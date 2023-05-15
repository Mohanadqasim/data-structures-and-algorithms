from stack_file import Stack

def validate_brackets(string):
    """
    Check if the brackets in the given string are balanced.

    Parameters:
    string (str): The string to check for balanced brackets.

    Returns:
    bool: True if the brackets are balanced, False otherwise.
    """

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
    """
    Check if the given opening and closing brackets match.

    Parameters:
    open_bracket (str): The opening bracket.
    close_bracket (str): The closing bracket.

    Returns:
    bool: True if the brackets match, False otherwise.
    """

    if open_bracket == "(" and close_bracket == ")":
        return True
    
    elif open_bracket == "{" and close_bracket == "}":
        return True
    
    elif open_bracket == "[" and close_bracket == "]":
        return True
    
    else:
        return False

    






print(validate_brackets("()[[Extra Characters]]"))
print(validate_brackets("{}{Code}[Fellows](())"))
print(validate_brackets("{(})"))
print(validate_brackets("[}"))