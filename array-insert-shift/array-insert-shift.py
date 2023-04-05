def insert_array(arr,n):
    idx=len(arr)//2
    arr.insert(idx,n)
    return arr

print(insert_array([2,4,6,-8], 5))
print(insert_array([42,8,15,23,42], 16))

def shift_array(arr):
    idx=len(arr)//2
    if idx%2==0:
        del arr[idx]
    else:
        del arr[idx-1]
    return arr

print(shift_array([1, 2, 3, 4, 5]))
print(shift_array(['a', 'b', 'c', 'd', 'e', 'f']))