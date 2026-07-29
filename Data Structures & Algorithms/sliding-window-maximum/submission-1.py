class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Output = []
        q = deque() #index
        l = 0
        for r in range(0,len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if (r+1)>=k:
                Output.append(nums[q[0]])
                l+=1
            if l>q[0]:
                q.popleft()
        return Output
            
        