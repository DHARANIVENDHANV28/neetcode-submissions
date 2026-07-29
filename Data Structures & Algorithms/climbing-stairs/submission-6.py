class Solution:
    def climbStairs(self, n: int) -> int:
        memo ={1:1,2:2}
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x]=f(x-1)+f(x-2)
                return memo[x]
        return f(n)



















        # output = 0
        # def dfs(x):
        #     nonlocal output
        #     if x>n:
        #         return 
        #     if x == n:
        #         output+=1 
        #         return
        #     dfs(x+1)
        #     dfs(x+2)
        # dfs(0)
        # return output
        