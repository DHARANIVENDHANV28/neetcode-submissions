class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = float("+inf")
        nums.sort()
        l = 0
        r = l+k-1
        while r < len(nums):
            diff = nums[r]-nums[l]
            res = min(res,diff)
            l += 1
            r = l+k-1
        return res
            
        