

class Solution:
    def climbStairs(self, n: int) -> int:
  
        output = 0

        def dfs(curr_step):
            nonlocal output  
            if curr_step == n:
                output += 1
                return
            if curr_step > n:
                return

            dfs(curr_step+1)
            dfs(curr_step+2)

        dfs(0)
        return output

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 3:
#             return n
#         n1, n2 = 2, 3

#         for i in range(4, n + 1):
#             temp = n1 + n2
#             n1 = n2
#             n2 = temp
#         return n2

