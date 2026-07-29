class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        curSum = 0
        hashmap = {0:1}
        for num in nums:
            curSum += num
            diff = curSum-k
            if diff in hashmap:
                output += hashmap[diff]
            if curSum in hashmap:
                hashmap[curSum] += 1
            else:
                hashmap[curSum] = 1
        return output


        