class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = [[-1]*2 for _ in range(len(nums))]

        def dfs(i,flag):
            if i>=len(nums) or (flag and i == len(nums)-1):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            memo[i][flag] = max(dfs(i+1,flag),nums[i]+dfs(i+2,flag or i==0))
            return memo[i][flag]
        return max(dfs(0,True),dfs(1,False))

































        # house = set()
        # loot_max = 0
        # def dfs(idx,loot):
        #     nonlocal loot_max
        #     if idx>=len(nums):
        #         loot_max = max(loot_max,loot)
        #         return
        #     if not (idx == len(nums)-1 and 0 in house):
        #         house.add(idx)
        #         dfs(idx+2,loot+nums[idx])
        #         house.remove(idx)
        #     dfs(idx+1,loot)
        # dfs(0,0)
        # return loot_max
        