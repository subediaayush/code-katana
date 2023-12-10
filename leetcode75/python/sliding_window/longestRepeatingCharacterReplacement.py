class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        maxLength = 0
        l = 0
        r = 0

        def findMaxFreq(c):
            max = 0
            for count in c:
                if c[count] > max:
                    max = c[count]

            return max

        while r < len(s):
            chars[s[r]] = chars.get(s[r], 0) + 1

            while r-l+1 - max(chars.values()) > k:
                chars[s[l]] = chars[s[l]] -1
                l += 1
            
            maxLength = max(maxLength, r-l+1)
            r+=1
            
        return maxLength

                
