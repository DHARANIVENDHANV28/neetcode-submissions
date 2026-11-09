class Solution:
    def isDecomposable(self, s: str) -> bool:
        l,r = 0,0
        n = len(s)
        two = 0
        while l<=r and r<n:
            while r<n and s[l]==s[r]:
                r+=1
            remainder = (r-l)%3 
            if remainder == 1:
                return False
            if remainder == 2:
                two+=1
            l = r
        return two==1


            
