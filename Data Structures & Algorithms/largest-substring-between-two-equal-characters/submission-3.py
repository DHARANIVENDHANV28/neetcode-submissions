class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxL = -1
        INDEX = {}
        for idx,ch in enumerate(s):
            if ch not in INDEX:
                INDEX[ch] = idx 
            else:
                maxL = max(maxL,idx-INDEX[ch]-1)
        return maxL 
        