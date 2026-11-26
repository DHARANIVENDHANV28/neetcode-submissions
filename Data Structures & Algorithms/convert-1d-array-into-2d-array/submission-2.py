class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if m*n != len(original):
            return res
        res = [[] for _ in range(m)]
        print(res)
        idx = -1
        for i in range(len(original)):
            if i%n==0:
                idx+=1
            res[idx].append(original[i])
        
        # for r in range(m):
        #     cols = []
        #     for c in range(n):
        #         first = original.pop(0)
        #         cols.append(first)
        #     res.append(cols)
        return res
