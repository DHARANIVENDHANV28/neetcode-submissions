class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        if k>=len(nums):
            k = len(nums)
        while i+k<=len(nums):
            if len(set(nums[i:i+k+1])) != len(nums[i:i+k+1]):
                return True
            i+=1
        return False
        