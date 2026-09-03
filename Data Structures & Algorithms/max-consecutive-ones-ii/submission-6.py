class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        l = 0
        cnt = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt+=1
            while cnt>1 and l<r:
                if nums[l] == 0:
                    cnt -= 1
                l+=1
            res = max(res,r-l+1)
        
        return res
            
            
            
            

            

































        # l = 0
        # zero = 0
        # res = 0
        # for r in range(len(nums)):
        #     if nums[r] == 0:
        #         zero += 1
        #     while zero > 1:
        #         if l<=r and nums[l] == 0:
        #             zero -= 1
        #         l += 1
        #         else:
        #             l += 1
        #     res = max(res,r-l+1)
        # return res


            
        
        