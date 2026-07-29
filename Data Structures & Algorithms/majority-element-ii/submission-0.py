class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        HashMap = {}
        n = len(nums)
        res = set()
        for num in nums:
            if num not in HashMap:
                HashMap[num] = 0
            HashMap[num]+=1
            if HashMap[num] > n//3:
                res.add(num)

        return list(res)
        