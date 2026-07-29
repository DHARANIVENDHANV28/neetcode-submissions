class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res= 0
        idx = 0
        for i,n in enumerate(nums):
            if n>=res:
                res = n
                idx = i
        return idx


        