class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx,n in enumerate(numbers):
            diff = target - n
            if diff not in hashmap:
                hashmap[n] = idx
            else:
                return [hashmap[diff]+1,idx+1]

        