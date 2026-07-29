class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, stack = [],[]
        

        def BackTracking(i):
            if i>= len(s):
                res.append(stack.copy())
                return True
            for j in range(i,len(s)):
                if self.palindrome(s[i:j+1]):
                    stack.append(s[i:j+1])
                    BackTracking(j+1) 
                    stack.pop()
        BackTracking(0)

        return res
    def palindrome(self,string):
            if string == string[::-1]:
                return True
            else:
                return False