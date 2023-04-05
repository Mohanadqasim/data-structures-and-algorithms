def reverse_array(arr):
    length=len(arr)-1
    new_arr=[]
    for items in arr:
        new_arr.append(arr[length])
        length-=1
    print(new_arr)


reverse_array([1, 2, 3, 4, 5, 6])
reverse_array([89, 2354, 3546, 23, 10, -923, 823, -12])
reverse_array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]	)


def reverse_arrayII(arr):
    current = 0
    length = len(arr) - 1
    while current < length:
        arr[current], arr[length] = arr[length], arr[current]
        current += 1
        length -= 1
    print(arr)



reverse_arrayII([1, 2, 3, 4, 5, 6])
reverse_arrayII([89, 2354, 3546, 23, 10, -923, 823, -12])
reverse_arrayII([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]	)