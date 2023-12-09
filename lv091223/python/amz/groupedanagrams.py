def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagrs = {}
    for str in strs:
        key = getKey(str)
        existing = anagrs.get(key, [])
        existing.append(str)
        print(key, existing)
        anagrs[key] = existing

    return list(anagrs.values())

def getKey(string):
    return str(sorted(string))

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))