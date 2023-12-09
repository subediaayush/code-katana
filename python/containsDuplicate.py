class Solution(object):
    def containsDuplicate(self, nums):
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
            if map[num] > 1:
                return False
        return True