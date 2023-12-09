class Solution(object):
    
    def twoSum(self, nums:[], target: int) -> []:
        nMap = {}
        for i in range(len(nums)):
            if nMap.get(target - nums[i], -1) != -1:
                return [i, nMap[target - nums[i]]]
            else:
                nMap[nums[i]] = i
