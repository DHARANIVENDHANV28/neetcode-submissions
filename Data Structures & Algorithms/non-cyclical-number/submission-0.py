class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def rec(num):
            print(seen,num)
            SumSq = 0
            for n in str(num):
                SumSq += int(n)**2
            if SumSq == 1:
                return True
            if SumSq in seen:
                return False
            seen.add(SumSq)
            if rec(SumSq):
                return True
            else:
                return False
        return rec(n)

        