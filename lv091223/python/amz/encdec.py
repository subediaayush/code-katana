class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        output = ''
        for i, str in enumerate(strs):
            output = output + ('' if i == 0 else '#') + self.encodeWord(str)

        return output
    
    def encodeWord(self, str):
        output = ''
        for i in range(len(str)):
            c = str[i]
            if c == '#':
                output += '^#'
            elif c == '^':
                output += '^^'
            else:
                output += c
        return output

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        output = []
        current = ''
        skip = False
        for i in range(len(str)):
            if skip: 
                skip = False
                continue

            c = str[i]
            if c == '^':
                if i == len(str) - 1:
                    raise 'Invalid String'
                else:
                    next = str[i+1]
                    if next == '#':
                        current += '#'
                    elif next == '^':
                        current += '^'
                    else:
                        raise 'Invalid String'                    
                skip = True
                continue
            elif c == '#':
                output.append(current)
                current = ''
            else:
                current += c

        if len(current) > 0:
            output.append(current)

        return output


input = ['hell^o#how', 'are', 'you']
encoded = Solution().encode(input)
decoded = Solution().decode(encoded)
print(input, decoded, encoded, input == decoded)