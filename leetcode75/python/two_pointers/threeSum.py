class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()

        sums = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            sums.extend(self.twoSums(nums, i + 1, nums[i]))
        
        return sums
    
    def twoSums(self, nums: [int], l: int, target: int) -> [[int]]:
        sums = []

        r = len(nums) - 1
        t = 0; sum = 0
        while l < r:
            sum = nums[l] + nums[r] + target
            if sum == 0:
                sums.append([target, nums[l], nums[r]])
            
            if sum <= 0:
                t = nums[l]
                while(t == nums[l] and r > l): l += 1
            
            if sum >= 0:
                t = nums[r]
                while(t == nums[r] and r > l): r -= 1                
            
        return sums