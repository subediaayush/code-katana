def oddNumbers(array: []):
    res = None
    for a in array:
        if res == None:
            res = a
        else:
            res = res ^ a
    return res


print(oddNumbers([1,2,3,4,4,9,2,1,9]))