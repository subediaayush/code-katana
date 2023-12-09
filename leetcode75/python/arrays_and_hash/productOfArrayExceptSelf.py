class Solution(object):
    def productExceptSelf(self, nums: [int]) -> [int]:
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            pre = pre * (1 if i == 0 else nums[i-1])
            res[i] = pre

        post = 1
        for j in range(len(nums) - 1, -1, -1):
            post = post * (1 if j == len(nums) - 1 else nums[j + 1])
            res[j] *= post

        return res