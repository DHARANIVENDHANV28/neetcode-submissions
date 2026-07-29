class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(idx,step):
            print(idx,step)
            if idx >= len(nums)-1:
                return True
            if step == 0 and idx<len(nums):
                return False
            for i in range(idx+1,idx+step+1):
                if i < len(nums):
                    if dfs(i,nums[i]):
                        return True
        return True if dfs(0,nums[0]) else False
                
                    

        