class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = [-1]*len(nums)
        def dfs(idx):
            if idx>=len(nums):
                return 0
            if memo[idx] != -1:
                return memo[idx]
            else:
                memo[idx] = max(dfs(idx+1),nums[idx]+dfs(idx+2))
                return memo[idx]
        return dfs(0) 




        # output = 0
        # def dfs(idx,cost):
        #     nonlocal output
        #     if idx>=len(nums):
        #         output = max(output,cost)
        #         return
        #     dfs(idx+2,cost+nums[idx])
        #     dfs(idx+1,cost)
        # dfs(0,0)
        # return output

        