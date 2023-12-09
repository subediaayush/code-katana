def permutations(array: []) -> []:   
    if (len(array) == 1): 
        return [array]

    result = []
    for i in range(len(array)):
        first = array.pop(0)
        perms = permutations(array[:])
        for perm in perms:
            perm.append(first)

        result.extend(perms)    
        array.append(first)

    return result

perms = permutations([1,3,5,7,9])
perms.sort()
print(perms)