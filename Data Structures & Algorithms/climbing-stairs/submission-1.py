# class Solution:
#     def climbStairs(self, n: int) -> int:
#         stack = []
#         output = 0  

#         def dfs(i):
            
#             if sum(stack)==n:
#                 output += 1
#                 return
#             if sum(stack)>n:
#                 return

#             stack.append(i)
#             dfs(1)
#             stack.pop()
#             dfs(2)

#         dfs(1)
#         return output

class Solution:
    def climbStairs(self, n: int) -> int:
  
        output = 0

        def dfs(curr_step):
            nonlocal output  # Ensures we're modifying the output from the outer scope
            if curr_step == n:
                output += 1
                return
            if curr_step > n:
                return

            dfs(curr_step+1)
            dfs(curr_step+2)

        dfs(0)
        return output
