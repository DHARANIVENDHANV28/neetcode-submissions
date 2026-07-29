class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        seen = set()
        ROWS,COLS = len(mat),len(mat)
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if r == c:
                    res += mat[r][c]
                    seen.add((r,c))
                elif r+c == ROWS-1 and (r,c) not in seen:
                    res += mat[r][c]
                    seen.add((r,c))

        return res

        