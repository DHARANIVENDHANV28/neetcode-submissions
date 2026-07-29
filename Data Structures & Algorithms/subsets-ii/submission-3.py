class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        def dfs(sub,idx):
            if idx>=len(nums):
                output.append(sub.copy())
                return
            sub.append(nums[idx])
            dfs(sub,idx+1)
            sub.pop()
            while idx+1<len(nums) and nums[idx+1] == nums[idx]:
                idx+=1
            dfs(sub,idx+1)
        dfs([],0)
        return output

            
        