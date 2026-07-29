class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        HashMap = {0:0}
        res = 0
        l = 0


        for r in range(len(nums)):
            if nums[r] == 0:
                HashMap[0] += 1
        
            while HashMap[0] > k:
                if nums[l] == 0:
                    HashMap[0] -= 1
                l += 1
            
            res = max(res,r-l+1)
        return res
                
        