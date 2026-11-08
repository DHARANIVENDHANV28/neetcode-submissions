class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        score = float('-inf')
        total = sum(nums)
        prefix = 0
        for n in nums:
            prefix += n
            suffix = total-prefix+n
            score = max(score,prefix,suffix)
        return score