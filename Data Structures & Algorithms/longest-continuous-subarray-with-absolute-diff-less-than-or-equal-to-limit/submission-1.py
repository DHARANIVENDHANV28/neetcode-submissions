class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        MAX,MIN = 0,0
        maxlen = 0
        l = 0

        for r in range(len(nums)):
            MAX = max(nums[l:r+1])
            MIN = min(nums[l:r+1])
            # print(nums[l:r+1])
            if MAX-MIN <= limit:
                # print("IN",nums[l:r+1],l,r)
                maxlen = max(maxlen,r-l+1)
            else:
                l += 1

        return maxlen

        