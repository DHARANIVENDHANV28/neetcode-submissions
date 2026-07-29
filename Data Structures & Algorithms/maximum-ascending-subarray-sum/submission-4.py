class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        SUM = nums[0]
        res = nums[0]
        for idx in range(1,len(nums)):
            if nums[idx] <= nums[idx-1]:
                SUM = 0
            SUM += nums[idx]
            res = max(res,SUM)
        return res
            
            
        