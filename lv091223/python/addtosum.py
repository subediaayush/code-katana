# Given an array of integers, find two numbers such that they add up to a specific target.

def addSum(array, target):
    # array = []
    array.sort()

    l = 0
    r = len(array) - 1

    while l < r:
        left = array[l]
        if left == target: 
            return []
        
        right = array[r]
        sum = left + right
        if sum == target:
            return [left, right]
        elif sum < target:
            l += 1
        else:
            r -= 1

    return []

print(addSum([1,2,3], 5))