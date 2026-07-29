class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for idx in range(len(s)):
            if idx+1 < len(s):
                res += abs(ord(s[idx])-ord(s[idx+1]))        
        return res