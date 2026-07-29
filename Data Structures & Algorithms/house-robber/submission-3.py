class Solution:
    def rob(self, nums: List[int]) -> int:
        memory = [-1]*len(nums)
        def dfs(i):
            if i<0:
                return 0
            if i==0:
                return nums[i]
            if memory[i] != -1:
                return memory[i]

            pick = dfs(i-2)+nums[i]
            not_pick = 0+dfs(i-1)
            memory[i] = max(pick,not_pick)
            return memory[i]
        return dfs(len(nums)-1)
