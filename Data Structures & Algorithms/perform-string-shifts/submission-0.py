class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        res = s
        tmp = [0]*len(s)
        for sh in shift:
            for i,ch in enumerate(res):
                if sh[0] == 1:
                    tmp[(i+sh[1])%len(s)] = ch
                else:
                    tmp[(i-sh[1])%len(s)] = ch
                
            res = tmp
            tmp = [0]*len(s)
        return "".join(res)



        