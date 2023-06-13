# Merge Sort

We will walk through the step-by-step execution of the Merge Sort algorithm using the provided pseudocode.

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```


### MergeSort:
1. Define a function called MergeSort that takes an array of integers called arr as an argument.

2. Declare a variable n and set it to the length of arr.

3. If n is greater than 1, do the following:

- Declare a variable mid and set it to n divided by 2.

- Declare a new array called left and set it to the subarray of arr from index 0 to mid (excluding mid).

- Declare a new array called right and set it to the subarray of arr from index mid to n (including mid).

- Recursively call MergeSort on the left array to sort it.

- Recursively call MergeSort on the right array to sort it.

- Call the Merge function with the left, right, and arr arrays to merge the sorted left and right sides together.

4. Exit the function.

### Merge:
1. Define a function called Merge that takes three arguments:

- An array of integers called left.

- An array of integers called right.

- An array of integers called arr.

2. Declare three variables: i, j, and k, and set them all to 0. These variables will be used as pointers to keep track of the indices in the left, right, and arr arrays, respectively.

3. Start a while loop with the following condition: while i is less than the length of the left array and j is less than the length of the right array.

4. Inside the while loop, do the following:

- Check if the value at index i in the left array is less than or equal to the value at index j in the right array.

- If the condition is true, set the value at index k in the arr array to the value at index i in the left array, increment i by 1, and increment k by 1.

- If the condition is false, set the value at index k in the arr array to the value at index j in the right array, increment j by 1, and increment k by 1.

5. After the while loop, check if i is equal to the length of the left array. If it is, it means that all the elements from the left array have been merged into the arr array. In this case, set the remaining entries in the arr array to the remaining values in


## Code Tracing 
![Alt text](./Untitled%20(17).jpg)