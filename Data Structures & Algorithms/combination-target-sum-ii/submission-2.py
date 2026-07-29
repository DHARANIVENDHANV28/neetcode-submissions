class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        def dfs(sub,Sum,idx):
            if idx>=len(candidates):
                if Sum == target:
                    output.append(sub.copy())
                return
            
            sub.append(candidates[idx])

            dfs(sub,Sum+candidates[idx],idx+1)
            sub.pop()
            while idx+1<len(candidates) and candidates[idx+1]==candidates[idx]:
                idx+=1
            dfs(sub,Sum,idx+1)

        dfs([],0,0)
        return output
        