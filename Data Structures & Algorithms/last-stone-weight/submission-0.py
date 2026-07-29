class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = stones
        while len(s) >=2:
            s = sorted(s)
            val1,val2 = s[-1],s[-2]
            s = s[:-2]
            if val1 > val2 or val2 > val1:
                s.append(abs(val1-val2))
        return s[0] if s else 0
        