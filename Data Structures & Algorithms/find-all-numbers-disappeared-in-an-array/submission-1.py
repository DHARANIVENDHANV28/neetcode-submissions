class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = max(nums)
        res = []

        for num in range(1,len(nums)+1):
            print(num)
            if num not in nums:
                res.append(num)

        return res
            
