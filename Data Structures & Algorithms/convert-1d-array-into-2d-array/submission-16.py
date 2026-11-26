class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        res = [[] for _ in range(m)]
        idx = -1
        for i in range(len(original)):
            if i%n==0:
                idx+=1
            res[idx].append(original[i])        
        return res
