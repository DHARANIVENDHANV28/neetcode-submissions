class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = set()
        res = []
        nums.sort()

        def dfs(sub):
            if len(sub)==n:
                res.append(sub.copy())
                return None
            
            for i in range(n):
                if i in visited:
                    continue
                # Skip duplicate choices at the same level
                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited:
                    continue
                visited.add(i)
                sub.append(nums[i])
                dfs(sub)
                sub.pop()
                visited.remove(i)
            return None

        dfs([])
        return res