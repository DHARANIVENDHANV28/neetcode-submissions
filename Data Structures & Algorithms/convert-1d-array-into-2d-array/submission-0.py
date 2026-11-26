class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if m*n != len(original):
            return res
        
        for r in range(m):
            cols = []
            for c in range(n):
                first = original.pop(0)
                cols.append(first)
            res.append(cols)
        return res
