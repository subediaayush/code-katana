class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i - 1] > nums[i]:
                continue
            break
        
        i-=1
        print('got', i)
        for j in range(len(nums) -1, i, -1):
            if (nums[i] < nums[j]):
                nums[i] = nums[i] ^ nums[j]
                nums[j] = nums[i] ^ nums[j]
                nums[i] = nums[i] ^ nums[j]
                # nums[i] = nums[j]
                # nums[j] = temp
                nums[i + 1:] = sorted(nums[i+1:])
                return

arr = [3,1,2]
arr = [3,2,1]
arr = [2,3,1]
Solution().nextPermutation(arr)
print(arr)