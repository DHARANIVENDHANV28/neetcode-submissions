class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(idx,permute,track):
            if idx >= len(nums):
                output.append(permute.copy())
                return
            for i in range(0,len(nums)):
                if i not in track :
                    track.append(i)
                    permute.append(nums[i])
                    dfs(idx+1,permute,track)
                    track.pop()
                    permute.pop()
                    
        dfs(0,[],[])
        unique = []
        for ele in output:
            if ele not in unique:
                unique.append(ele)
        return unique