def rotateArray(array):
    for i in range(len(array)):
        array[i] = array[i+1]
    return array

print(rotateArray([1,2,3,4,5,6,7,8,9]))