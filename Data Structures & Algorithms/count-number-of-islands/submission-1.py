class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        seen = set()
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        island = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= row or c >= col or
                grid[r][c] == "0" or (r, c) in seen):
                return
            
            seen.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    island += 1

        return island
