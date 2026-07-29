class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat = []
        for row in matrix:
            mat+=row
        l,r = 0,len(mat)-1
        while l<=r:
            m = l+((r-l)//2)
            if mat[m] > target:
                r = m-1
            elif mat[m] < target:
                l = m+1
            else:
                return True
        return False