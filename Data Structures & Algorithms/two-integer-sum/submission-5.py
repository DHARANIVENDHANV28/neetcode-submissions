class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx,num in enumerate(nums):
            diff = target-num
            if diff not in hashmap:
                hashmap[num] = idx
            else:
                return [hashmap[diff],idx]