class Solution:
    def minOperations(self, s: str) -> int:
        Zero = ["0" if i%2==0 else "1" for i in range(len(s))]
        One = ["0" if i%2!=0 else "1" for i in range(len(s))]
        Zval = 0
        Oval = 0
        for i in range(len(s)):
            if s[i] != Zero[i]:
                Zval += 1
            if s[i] != One[i]:
                Oval += 1

        return min(Zval,Oval)
        