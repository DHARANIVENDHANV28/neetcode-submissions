class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(sub,idx):
            if idx >= len(nums):
                if len(sub) == len(nums):
                    output.append(sub.copy())
                return 
            for i in nums:
                if i not in sub:
                    sub.append(i)
                    dfs(sub,idx+1)
                    sub.pop()
        dfs([],0)
        return output
        