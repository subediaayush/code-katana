class Solution(object):
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        aMap = {}
        for str in strs:
            key = self.getKey(str)
            ex = aMap.get(key, [])
            ex.append(str)
            aMap[key] = ex


        output = []
        for grp in aMap:
            output.append(aMap[grp])
        
        return output

    def getKey(self, inp):
        return str(sorted([c for c in inp]))