class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        NS = 0
        for i in range(1,n+1):
            NS = NS+i
            if NS>n:
                return res
            res += 1
        return res
        


        