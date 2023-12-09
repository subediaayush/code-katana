class Solution(object):
    def longestConsecutive(self, nums: [int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1

        nums.sort()

        count = 0
        maxCount = 0
        l = 0
        r = len(nums) - 1

        for l in range(len(nums) - 1):
            if nums[l+1] - nums[l] == 1:
                count += 1
            elif nums[l + 1] - nums[l] > 1:
                if count + 1 > maxCount:
                    maxCount = count + 1

                count = 0
        
        if count + 1 > maxCount:
            maxCount = count + 1

        return maxCount
    
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(Solution().longestConsecutive([-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7]))