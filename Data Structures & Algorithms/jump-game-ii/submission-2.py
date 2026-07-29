class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(idx):
            if idx == len(nums)-1:
                return 0
            if idx in memo:
                return memo[idx]

            minJump = float('inf')
            
            for i in range(idx+1,idx+nums[idx]+1):
                if i < len(nums):
                    minJump = min(minJump,1+dfs(i))
            memo[idx] = minJump
            return memo[idx]
        return dfs(0)
        
        
        