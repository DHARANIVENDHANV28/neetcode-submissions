class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = float("-inf")

        for i in range(len(nums)):
            pro = nums[i]
            output = max(output,pro)

            for j in nums[i+1:]:
                pro = pro*j
                output = max(output,pro)
        # output = max(output,nums[-1])
        return output    
                

        