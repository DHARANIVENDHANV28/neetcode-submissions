class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):
            if (r<0) or (c<0) or (r>=ROWS) or (c>=COLS) or ((r,c) in visited) or (grid[r][c] == 0):
                return 
            if (r==0) or (r==ROWS-1) or (c==0) or (c==COLS-1):
                return True
            visited.add((r,c))
            for dr,dc in directions:
                if dfs(r+dr,c+dc):
                    return True
            return False

        Output = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    visited = set()
                    if not dfs(r,c):
                        Output+=1
        return Output
