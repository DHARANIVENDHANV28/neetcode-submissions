class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        HashMap = {}
        for ch in s:
            if ch not in HashMap:
                HashMap[ch] = 0
            HashMap[ch] += 1
        
        odd = 0

        for k,v in HashMap.items():
            if v%2 != 0:
                odd += 1
            if odd > 1:
                return False
        return True