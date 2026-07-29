class Solution:
    def longestPalindrome(self, s: str) -> int:
        HashMap = {}

        for ch in s:
            if ch not in HashMap:
                HashMap[ch] = 0
            HashMap[ch] += 1

        print(HashMap) 
        
        res = 0
        odd = False
        for k,v in HashMap.items():
            if v%2 == 0: #EVEN
                res += v
            else:
                res += v-1
                odd = True
        
        if odd:
            res += 1
        
        
        return res
