class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        HashMap = {}
        def dfs(Sum,idx):
            if Sum == total-Sum:
                return True
            if (Sum,idx) in HashMap:
                return HashMap[(Sum,idx)]
            if idx>=len(nums) or Sum>(total-Sum):
                return False

            res = (dfs(Sum+nums[idx],idx+1) or dfs(Sum,idx+1))
            HashMap[(Sum,idx)] = res
            return res
        return dfs(0,0)
        