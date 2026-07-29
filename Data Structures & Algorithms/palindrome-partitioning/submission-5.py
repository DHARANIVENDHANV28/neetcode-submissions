class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []

        def dfs(sub, idx):
            if idx>=len(s):
                output.append(sub.copy())
                return 
            for j in range(idx,len(s)):
                if self.isPalindrome(s,idx,j):
                    sub.append(s[idx:j+1])
                    dfs(sub,j+1)
                    sub.pop()
        dfs([],0)
        return output

    def isPalindrome(self,s,l,r):
        while l<r:
            if s[l] != s[r]:
                return False
            l = l+1
            r = r-1
        return True