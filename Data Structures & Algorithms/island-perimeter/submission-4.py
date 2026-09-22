class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        seen = set()
        perimeter = 0

        def dfs(x, y):
            nonlocal perimeter
            
            if x < 0 or y < 0 or x >= row or y >= col or grid[x][y]==0:
                perimeter += 1
                return
            
            if (x, y) in seen:
                return
            
            seen.add((x, y))
            
            for dx, dy in direction:
                dfs(x + dx, y + dy)

        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    dfs(x, y)
                    return perimeter