# Array Binary Search

## proplem domain
Write a function called binary-search which takes in 2 parameters: a sorted array and the search key, and return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Example

### Input
[4, 8, 15, 16, 23, 42], 15

[-131, -82, 0, 27, 42, 68, 179], 42

[11, 22, 33, 44, 55, 66, 77], 90

[1, 2, 3, 5, 6, 7], 4

### Output
2

4

-1

-1


### The pseudocode if the array contained objects (sorted on a given property), and you were searching for certain property value:

```
function binary-search-objects(arr, property, n):
    l = 0
    r = length of arr - 1

    while l <= r:
        mid = (l + r) // 2
        midValue = arr[mid][property] 

        if midValue == n:
            return mid
        elif midValue < n:
            l = mid + 1
        else:
            r = mid - 1

    return -1

```