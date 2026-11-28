class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ROWS,COLS = len(matrix),len(matrix[0])
        minRows,maxCols = set(),set()

        for r in range(ROWS):
            minRows.add(min(matrix[r]))
        for c in range(COLS):
            MAX = 0
            for r in range(ROWS):
                MAX = max(MAX,matrix[r][c])
            maxCols.add(MAX)

        res = []
        for num in minRows:
            if num in maxCols:
                res.append(num)
        return res

