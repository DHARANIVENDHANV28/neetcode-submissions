class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        res = 1
        for i in range(1,abs(n)+1):
            res = x*res
        if n>0:
            return res
        if n<0:
            return 1/res
        