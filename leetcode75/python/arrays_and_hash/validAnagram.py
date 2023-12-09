class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != range(len(t)):
            return False
        
        sMap = {}
        tMap = {}

        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        return sMap == tMap


        