class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) == 0 or s is None or words is None:  
            return []


        count = {}
        wordLength = len(words[0])
        res = []
        wordsLength = wordLength * len(words)

        for word in words:
            count[word] = count.get(word, 0) + 1
        
        for left in range(len(s) - wordsLength + 1):
            wordsSeen = {}
            for right in range(len(words)):
                wordIndex = left + right * wordLength
                tempWord = s[wordIndex : wordLength + wordIndex]
                
                if tempWord not in count:
                    break

                wordsSeen[tempWord] = wordsSeen.get(tempWord, 0) + 1

                if wordsSeen[tempWord] > count[tempWord]:
                    break
                
            if wordsSeen == count: 
                res.append(left)

        return res

def isEmpty(dict):
    for value in dict.values():
        if value != 0: return False
    return True
    
print(Solution().findSubstring('barfoofoobarthefoobarman', ["bar","foo","the"]))