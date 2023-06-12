def Insert(sorted, value):
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