class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        HashMap = {}
        for n in nums:
            if n not in HashMap:
                HashMap[n] = 1
            else:
                HashMap[n] += 1

        for k,v in HashMap.items():
            res += v*(v-1)//2
        return res
            