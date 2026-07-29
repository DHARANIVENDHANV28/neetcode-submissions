class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        print(nums)
        output = []
        def dfs(idx,sub):
            if len(sub) == k:
                output.append(sub.copy())
                return 
            for i in range(idx,n):
                    sub.append(nums[i])
                    dfs(i+1,sub)
                    sub.pop()
        dfs(0,[])
        return output
        