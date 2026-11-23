class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays=sorted(arrays)
        fs,fe = arrays[0][0],arrays[0][-1]
        res = float('-inf')
        for ele in arrays[1:]:
            res = max(res,abs(fs-ele[-1]),abs(fe-ele[0]))
        return res
        