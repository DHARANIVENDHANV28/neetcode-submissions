class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    FOUND = False
                    for c1 in range(COLS):
                        if c1==c:
                            continue
                        if grid[r][c1] == 1:
                            res+=1
                            FOUND = True
                            break
                    if not FOUND:
                        for r1 in range(ROWS):
                            if r1==r:
                                continue
                            if grid[r1][c] == 1:
                                res+=1
                                break
        return res  
        