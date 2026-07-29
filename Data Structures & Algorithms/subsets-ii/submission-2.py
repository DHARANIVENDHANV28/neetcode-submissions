# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         out,subset = [],[]
#         def dfs(idx,subset):
#             if idx ==len(nums):
#                 out.append(subset.copy())
#                 return 
#             else:
#                 subset.append(nums[idx])
#                 dfs(idx+1,subset)
#                 subset.pop()
#                 while idx+1<len(nums) and nums[idx]==nums[idx+1]:
#                     idx += 1
#                 dfs(idx+1,subset)
#         dfs(0,[])
#         return out

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

        