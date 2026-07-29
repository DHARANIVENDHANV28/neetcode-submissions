class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def dfs(idx,sub,Sum):
            if Sum>=target:
                if Sum == target:
                    output.append(sub.copy())
                return
            if idx>=len(nums):
                return
            sub.append(nums[idx])
            dfs(idx,sub,Sum+nums[idx])
            sub.pop()
            dfs(idx+1,sub,Sum)
        dfs(0,[],0)
        return output
        