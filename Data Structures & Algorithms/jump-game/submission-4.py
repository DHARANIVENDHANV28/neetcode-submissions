class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if i+nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
        # def dfs(idx,step):
        #     if idx >= len(nums)-1:
        #         return True
        #     if step == 0 and idx<len(nums):
        #         return False
        #     for i in range(idx+1,idx+step+1):
        #         if i < len(nums):
        #             if dfs(i,nums[i]):
        #                 return True
        # return True if dfs(0,nums[0]) else False
                
                    

        