class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        prefix = 0
        count = {0:1}

        for n in nums:
            prefix += n
            if prefix-goal in count:
                res += count[prefix-goal]
            if prefix in count:
                count[prefix] += 1
            else: 
                count[prefix] = 1
        
        return res
       
        