class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        HashMap = {}

        for n in nums:
            if n not in HashMap:
                HashMap[n] = 0
            HashMap[n] += 1
        
        val = -1
        for k,v in HashMap.items():
            if v == 1:
                val = max(val,k)
        return val
        