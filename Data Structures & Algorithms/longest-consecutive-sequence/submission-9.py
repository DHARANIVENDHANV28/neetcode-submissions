class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        S_nums = sorted(set(nums))
        i = 0
        j = i+1
        Output = 0
        while i<j and j<len(S_nums):
            if (S_nums[j] == S_nums[j-1]+1):
                j+=1
            else:
                Output = max(Output,len(S_nums[i:j]))
                i = j
                j = i+1
        Output = max(Output,len(S_nums[i:j]))
        return Output
        