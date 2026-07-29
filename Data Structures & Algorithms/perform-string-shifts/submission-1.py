class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        net = 0
        for Dir,Amt in shift:
            if Dir == 0:
                net -= Amt
            else:
                net += Amt
        
        net = net%len(s)
        return s[-net:]+s[:-net]




        