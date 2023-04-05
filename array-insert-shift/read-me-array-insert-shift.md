# Array Insert Shift

## proplem domain
Write a function called insert-array which takes in an array and a value to be added. and return an array with the new value added at the middle index.

Write a function called shift-array which removes an element from the middle index and shifts other elements in the array to fill the new gap

## Example

### insert-array
### Input
[2,4,6,-8], 5

[42,8,15,23,42], 16

### Output
[2,4,5,6,-8]

[42,8,15,16,23,42]

### shift-array
### Input
[10, 20, 30]

['a', 'b', 'c', 'd', 'e', 'f']


### Output
[10, 30]

['a', 'b', 'd', 'e', 'f']



## Approach & Efficiency
I used the Single-responsibilty prenciple,with a Big O of O(N).