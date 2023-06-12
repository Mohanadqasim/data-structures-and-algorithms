# Sorting & Insertion
We will walk through the step-by-step execution of the Insertion Sort algorithm using the provided pseudocode.

```
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted
```

### InsertionSort:

1. define a function called InsertionSort that takes an array of integers called input as an argument

2. declare an empty array called sorted

3. set the value of sorted[0] to the value of input[0]   

4. start a while loop following this condition (for i=1 till i=input.length)

- Call Insert function with the following inputs(sorted,input[i]) till the condition is met.

6. after getting out of the while loop return storted array 

### Insert:

1. declare a function called insert that takes 2 arguments

- an array of integers called sorted

- an integer called value

2. declare a variable called i with value of 0

3. start a while loop with the following condition (value < sorted[i]), the while loop has to find the index of the closest number to value and yet the founded number must be less than value 

4. start a new while loop with the following condition(i<sorted.length)

- inside the while loop declare a new variable called temp and set its value to sorted[i] (the number that we found from the previous while loop)

- change the value of value (the argument) to sorted[i]

- change the value of temp to the value of value

- increase i by 1

5. Append value to sorted array.