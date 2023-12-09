def anagram(s,t):

    s1 = []
    for c in s:
        s1.append(c)

    s2 = []
    for c in t:
        s2.append(c)

    s1.sort()
    s2.sort()
    print (s1, s2)    
    return s1 == s2

print(anagram('anagram', 'nagaram'))