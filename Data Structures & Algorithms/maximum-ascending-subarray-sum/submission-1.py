class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        SUM = nums[0]
        res = nums[0]
        for idx in range(1,len(nums)):
            if nums[idx-1] < nums[idx]:
                SUM += nums[idx]
            else:
                SUM = nums[idx]
            res = max(res,SUM)
        return res
            
            
        