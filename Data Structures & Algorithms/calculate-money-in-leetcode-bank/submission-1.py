class Solution:
    def totalMoney(self, n: int) -> int:
        start = -1
        tmp,res = 0,0
        for i in range(n):
            if i%7==0:
                start+=1 
                tmp = start
            tmp+=1
            res+=tmp
        return res
            
