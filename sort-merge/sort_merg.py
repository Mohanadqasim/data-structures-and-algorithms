def merge_sort(arr):
    """
    Sorts an array using the Mergesort algorithm.

    Parameters:
    - arr (list): The array to be sorted.

    Returns:
    - list: The sorted array.
    """

    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        return merge(left, right, arr)


def merge(left, right, arr):
    """
    Merges two sorted subarrays into a single sorted array.

    Parameters:
    - left (list): The left subarray.
    - right (list): The right subarray.
    - arr (list): The array to store the merged result.

    Returns:
    - list: The merged and sorted array.
    """

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


# print(merge_sort([50,10]))
# print(merge_sort([8,4,23,42,16,15]))
# print(merge_sort([20,18,12,8,5,-2]))
# print(merge_sort([5,12,7,5,5,7]))
# print(merge_sort([2,3,5,7,13,11]))