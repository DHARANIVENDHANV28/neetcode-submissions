class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        l = 0
        r = len(res)-1

        for i in range(len(nums)):
            if nums[i]%2 == 0: #EVEN
                res[l] = nums[i]
                l+=1
            else: #ODD
                res[r] = nums[i]
                r-=1
        
        return res
        