class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        n = len(nums)
        score = float('-inf')
        l,r = 0,0
        res = 0
        while l < n:
            if r < n:
                res+=nums[r]
                r+=1
            elif l<n-1:
                res-=nums[l]
                l+=1
            else:
                break
            score = max(res,score)
            # print(l,r,nums[l:r+1],score)
        return score
        
