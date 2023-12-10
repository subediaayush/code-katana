class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        maxLength = 0
        l = 0
        r = 0

        while l <= r and r < len(s):
            chars[s[r]] = chars.get(s[r], 0) + 1

            while chars[s[r]] > 1:
                chars[s[l]] -= 1
                l += 1
            
            length = r - l + 1
            if length > maxLength:
                maxLength = length

            r += 1

        return maxLength

                
