def stringUnique(string):
    container = {}
    string = string.lower()
    for char in string:
        container[char] = 1

    print(container)
    return len(container) == len(string)

print(stringUnique('Rajesh'))