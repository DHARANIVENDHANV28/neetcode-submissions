class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        arr = sorted(candidates)
        def BT (ind,sub,sum_):
            if ind >= len(arr):
                if sum_==target:
                    output.append(sub.copy())
                return 
            if sum_ == target:
                output.append(sub.copy())
                return 
            for i in range(ind,len(arr)):
                if arr[i] == arr[i-1] and i>ind:
                    continue
                sub.append(arr[i])
                BT(i+1,sub,sum_+arr[i])
                sub.pop()
        BT(0,[],0)
        return output
