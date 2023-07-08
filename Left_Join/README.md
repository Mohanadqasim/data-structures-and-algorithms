# Proplem Domain

Write a function called left join

- Arguments: two hash maps
- The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
- The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

# Big O

- Time Complexity: O(n)
- Space Complexity: O(n)

# Solution

```
def left_join(synonyms, antonyms):
    result = {}

    for key in synonyms:
        if key in antonyms:
            result[key] = (synonyms[key], antonyms[key])
        else:
            result[key] = (synonyms[key], None)

    return result
```