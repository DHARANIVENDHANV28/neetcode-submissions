class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(sub,idx):
            if idx >= len(nums):
                output.append(sub.copy())
                return
            sub.append(nums[idx])
            dfs(sub,idx+1)
            sub.pop()
            dfs(sub,idx+1)
        dfs([],0)
        return output