class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0,0]
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1

        for i in range(1,len(nums)+1):
            if i not in count:
                count[i] = 0
            if count[i] == 0:
                res[1] = i
            if count[i] == 2:
                res[0] = i

        return res