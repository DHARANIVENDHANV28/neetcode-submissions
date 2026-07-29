class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        def dfs(Sum,idx):
            if idx>=len(nums):
                print(Sum,idx)
                if Sum == total-Sum:
                    return True
                return False
            return (dfs(Sum+nums[idx],idx+1) or dfs(Sum,idx+1))
        return dfs(0,0)
        