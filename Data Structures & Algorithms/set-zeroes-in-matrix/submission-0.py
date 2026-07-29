class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeros.append((r,c))
        for z in zeros:
            m,n = z[0],z[1]
            for r in range(rows):
                for c in range(cols):
                    if r == m or c == n:
                        matrix[r][c] = 0
        print(matrix)
        print(zeros)
                    
        
        