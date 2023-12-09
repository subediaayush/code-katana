class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == haystack: return 0
        hlen = len(haystack)
        nlen = len(needle)
        if nlen >= hlen: return -1
        
        for i in range(hlen - nlen + 1):
            obt = haystack[i:i+nlen]
            if obt == needle:
                return i
        return -1
        
print(Solution().strStr('abc', 'c'))