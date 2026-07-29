class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1
        res = 1000
        while l<r:
            m = l +(r-l)//2
            res = min(res,nums[m])
            if nums[m]>nums[r]:
                l = m+1
            else:
                r = m-1
        return min(res,nums[l])
       
        