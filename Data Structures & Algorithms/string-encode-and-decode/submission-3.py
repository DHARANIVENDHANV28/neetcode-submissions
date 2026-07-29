class Solution:

    def encode(self, strs: List[str]) -> str:
        # format: "<length>#<string>" for each string
        encoded = ''
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find the separator #
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # extract the string of 'length' characters after '#'
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res

