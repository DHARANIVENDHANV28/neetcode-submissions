class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        small = min(nums)
        HashMap = {i:0 for i in range(small,small+len(nums))}
        for n in nums:
            if n not in HashMap:
                return False
            HashMap[n]+=1
            if HashMap[n]>1:
                return False
        return True