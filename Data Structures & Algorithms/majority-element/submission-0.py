class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        majority = len(nums)//2

        for n in nums:
            
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
            if hashmap[n] > majority:
                return n


        