def binary_search(arr, n):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            l = mid + 1
        else:
            r = mid - 1
    return -1



print(binary_search([4, 8, 15, 16, 23, 42],15))

print(binary_search([-131, -82, 0, 27, 42, 68, 179],42))

print(binary_search([11, 22, 33, 44, 55, 66, 77],90))

print(binary_search([1, 2, 3, 5, 6, 7],4))


