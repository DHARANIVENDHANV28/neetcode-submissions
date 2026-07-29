class Solution:
    def firstUniqChar(self, s: str) -> int:
        HashMap = {}

        for ch in s:
            if ch not in HashMap:
                HashMap[ch] = 0
            HashMap[ch] += 1

        
        for idx,ch in enumerate(s):
            if HashMap[ch] == 1:
                return idx
        
        return -1  
        