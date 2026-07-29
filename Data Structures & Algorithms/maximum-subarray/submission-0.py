class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(nums):
                return float("-inf")

            if i in memo:
                return memo[i]

            # either extend subarray or start new
            memo[i] = max(nums[i], nums[i] + dfs(i+1))
            return memo[i]

        res = float("-inf")

        for i in range(len(nums)):
            res = max(res, dfs(i))

        return res
        