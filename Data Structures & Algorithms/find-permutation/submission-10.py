class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = []
        res = []
        n = len(s)

        for i in range(0,n+1):
            stack.append(i+1)

            if i == n or s[i] == 'I':
                while stack:
                    res.append(stack.pop())
        
        return res