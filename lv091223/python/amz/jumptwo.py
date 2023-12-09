values = {}

def jump(nums: [int]) -> int:
    return findMinJump(nums, 0)

def findMinJump(nums: [int], start: int):
    if values.get(start) != None:
        jmp = values[start]
        print('CACH from {} with value {} cost: {}'.format(start, nums[start], jmp))
        return jmp
    elif start == len(nums) - 1:
        return 0

    startValue = nums[start]
    minJump = None
    while startValue > 0:
        jump = findMinJump(nums, start + startValue)
        startValue -= 1
        if not minJump or jump < minJump:
            if (start + startValue == len(nums) - 1):
                break
            minJump = jump
    
    # print('jumping', nums[start], start, minJump + 1)
    values[start] = minJump + 1
    return minJump + 1

input =[2,3,1,1,4]
print(input)
print(jump(input))