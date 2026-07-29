class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        res = 0
        for l in range(0,len(s)-k+1):
            if len(set(s[l:l+k])) == k:
                # print(s[l:l+k])
                res+=1
            # print(s[l:l+k])
        
        return res

            
        