class Solution(object):
    def maxArea(self, height: [int]) -> int:
        maxArea = 0; l = 0; r = len(height) - 1
        while l < r:
            if (r - l) * min(height[l], height[r]) > maxArea:
                maxArea = (r - l) * min(height[l], height[r])
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea