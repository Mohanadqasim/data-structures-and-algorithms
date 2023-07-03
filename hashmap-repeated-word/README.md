# hashmap repeated word

## Problem Domain
Write a function called repeated word, that finds the first word that occurs more than once in a given string.

## Big O Notation
- Time Complexity: O(n)
- Space Complexity: O(n)

## Code
```
import string
def repeated_word(input_string):
    translator = str.maketrans('', '', string.punctuation)
    input_string = input_string.lower().translate(translator)
    words = input_string.split()
    encountered = set()
    for word in words:
        if word in encountered:
            return word
        else:
            encountered.add(word)
    return None
```