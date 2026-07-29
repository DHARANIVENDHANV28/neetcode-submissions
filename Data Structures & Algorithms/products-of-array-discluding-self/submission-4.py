class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums)):
            ans = 1
            lis = nums[:i]+nums[i+1:]
            for j in lis:
                ans *= j
            output.append(ans)
        return output


        