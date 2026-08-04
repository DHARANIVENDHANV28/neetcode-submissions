class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        res = []
        for n in nums:
            quad = a*(n**2) + b*n + c
            print(quad)
            res.append(quad)
        return sorted(res)
        