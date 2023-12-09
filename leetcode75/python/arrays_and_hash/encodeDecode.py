class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ''
        for word in strs:
            encoded += str(len(word)) + '#' + word

        return encoded

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """

        decoded = []
        countStr = ''
        idx = 0
        while(idx < len(s)):
            c = s[idx]
            if c >= '0' and c <= '9':
                countStr += c
                idx += 1
                continue
            elif c == '#':
                count = int(countStr)
                countStr = ''
                if count == 0:
                    decoded.append('')
                    idx += 1
                else:
                    decoded.append(s[idx + 1 : idx + 1 + count])
                    idx += 1 + count
        
        return decoded

        


# Your Codec object will be instantiated and called as such:
codec = Codec()
encoded = codec.encode(["V","Grz/"])
encoded = codec.encode(["Word","Hello"])
encoded = codec.encode(["Word","Hello", "#432"])
encoded = codec.encode(["","Hello", "#432"])
decoded = codec.decode(encoded)

print(encoded, decoded)