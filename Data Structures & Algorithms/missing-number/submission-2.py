class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(0,len(nums)):
            if i&nums[i]!=nums[i]:
                return i
            if i+1>=len(nums):
                return i+1

        