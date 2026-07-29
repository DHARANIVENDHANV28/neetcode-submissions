class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        output = []
        res = 0
        def dfs(sub,idx):
            nonlocal output
            nonlocal res
            if idx>=len(nums):
            # if sub and sub[-1] >= nums[idx]:
                res=max(res,len(sub))
                output.append(sub.copy())
                return
            if not sub or sub[-1] < nums[idx]:
                sub.append(nums[idx])
                dfs(sub,idx+1)
                sub.pop()
            dfs(sub,idx+1)

        dfs([],0)
        print(output)
        return res