# Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = None
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == temp:
                nums.pop(i)
            else:
                temp = nums[i]
        return nums
    
print(Solution().removeDuplicates([1,2,3,4,4]))        
