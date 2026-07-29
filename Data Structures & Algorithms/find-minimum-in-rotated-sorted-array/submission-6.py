class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if nums[l]<nums[r]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]
        else:
            while l<=r:
                m = l+((r-l)//2)
                if nums[m] < nums[m-1]:
                    return nums[m]
                else:
                    if nums[m]<nums[r]:
                        r=m-1
                    else:
                        l=m+1
            