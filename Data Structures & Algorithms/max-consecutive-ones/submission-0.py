class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prod = 1
        output = 0
        res = -1
        for n in nums:
            if n == 1:
                output+=1
            else:
                output = 0
            res = max(res,output)
        return res

            


                
        