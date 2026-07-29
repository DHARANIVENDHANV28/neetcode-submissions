class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        MAX = deque() #monotonically decreasing
        MIN = deque() #monotonically increasing
        maxlen = 0
        l = 0

        for r in range(len(nums)):

            while MIN and nums[r] < MIN[-1]:
                MIN.pop()
            
            while MAX and nums[r] > MAX[-1]:
                MAX.pop()

            MIN.append(nums[r])
            MAX.append(nums[r])

            while MAX and MIN and MAX[0] - MIN[0] > limit:
                if nums[l] == MAX[0]:
                    MAX.popleft()
                if nums[l] == MIN[0]:
                    MIN.popleft()
                l+=1
            maxlen = max(maxlen,r-l+1)
            
        return maxlen

        