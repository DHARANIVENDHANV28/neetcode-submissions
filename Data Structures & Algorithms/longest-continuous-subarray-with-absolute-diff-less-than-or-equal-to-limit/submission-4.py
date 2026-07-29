class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        MAX,MIN = nums[0],nums[0]
        maxlen = 0
        l = 0

        for r in range(len(nums)):
            MAX = max(MAX,nums[r])
            MIN = min(MIN,nums[r])
            print(nums[l:r+1],"MAX:",MAX,"MIN:",MIN)
            if MAX-MIN <= limit:
                print("IN",nums[l:r+1],l,r)
                maxlen = max(maxlen,r-l+1)
            else:
                if nums[l] == MAX:
                    MAX = max(nums[l+1:r+1])
                if nums[l] == MIN:
                    MIN = min(nums[l+1:r+1])
                l += 1

        return maxlen

        