class Solution:
    def jump(self, nums: List[int]) -> int:
        minJump = float('inf')
        def dfs(idx,jump):
            nonlocal minJump
            if idx == len(nums)-1:
                minJump = min(jump,minJump)
                return 
            if idx < len(nums):
                for i in range(idx,idx+nums[idx]):
                    dfs(i+1,jump+1)
        dfs(0,0)
        return minJump
        