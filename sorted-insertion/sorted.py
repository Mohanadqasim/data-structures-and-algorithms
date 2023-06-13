def Insert(sorted, value):
    """
    Inserts a value into a sorted list in ascending order.

    Args:
        sorted (list): A sorted list of values.
        value: The value to be inserted into the sorted list.

    Returns:
        None
    """
    i = 0
    while i < len(sorted) and value > sorted[i]:
        i += 1
    while i < len(sorted):
        temp = sorted[i]
        sorted[i] = value
        value = temp
        i += 1
    sorted.append(value)


def InsertionSort(input):
    """
    Sorts a list of values using the insertion sort algorithm.

    Args:
        input (list): The list of values to be sorted.

    Returns:
        list: The sorted list of values.
    """
    sorted = []
    if len(input):
        sorted.append(input[0])
        for i in range(1, len(input)):
            Insert(sorted, input[i])
        return sorted
    else:
        return([])




print(InsertionSort([50,10]))
# print(InsertionSort([8,4,23,42,16,15]))
# print(InsertionSort([20,18,12,8,5,-2]))
# print(InsertionSort([5,12,7,5,5,7]))
# print(InsertionSort([2,3,5,7,13,11]))