class Solution:
    def totalMoney(self, n: int) -> int:
        mondaydeposit = -1
        dailydeposit,res = 0,0
        for i in range(n):
            if i%7==0:
                mondaydeposit+=1 
                dailydeposit = mondaydeposit
            dailydeposit+=1
            res+=dailydeposit
        return res
            
