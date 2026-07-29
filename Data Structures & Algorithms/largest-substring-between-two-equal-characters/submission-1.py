class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxL = 0
        INDEX = {}
        FOUND = False
        for idx,ch in enumerate(s):
            # print(INDEX,maxL)
            if ch not in INDEX:
                INDEX[ch] = idx 
            else:
                FOUND = True
                maxL = max(maxL,idx-INDEX[ch]-1)
                # INDEX[ch] = idx
        return maxL if FOUND else -1
        