class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        HashMap = {}
        def dfs(cur,prev):
            if cur >= len(nums):
                return 0
            if (cur,prev) in HashMap:
                return HashMap[(cur,prev)]
            func = 0
            if prev == -1 or nums[prev]<nums[cur]:    
                func = 1+dfs(cur+1,cur)
            func = max(func,dfs(cur+1,prev))
            HashMap[(cur,prev)] = func
            return HashMap[(cur,prev)]
        return dfs(0,-1)














        # output = []
        # res = 0
        # def dfs(sub,idx):
        #     nonlocal output
        #     nonlocal res
        #     if idx>=len(nums):
        #     # if sub and sub[-1] >= nums[idx]:
        #         res=max(res,len(sub))
        #         output.append(sub.copy())
        #         return
        #     if not sub or sub[-1] < nums[idx]:
        #         sub.append(nums[idx])
        #         dfs(sub,idx+1)
        #         sub.pop()
        #     dfs(sub,idx+1)

        # dfs([],0)
        # print(output)
        # return res