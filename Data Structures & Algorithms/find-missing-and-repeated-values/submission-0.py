class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = []
        ROWS,COLS = len(grid),len(grid)
        seen = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] not in seen:
                    seen.add(grid[r][c])
                else:
                    res.append(grid[r][c])

        for n in range(1,(ROWS**2)+1):
            if n not in seen:
                res.append(n)
        return res


        