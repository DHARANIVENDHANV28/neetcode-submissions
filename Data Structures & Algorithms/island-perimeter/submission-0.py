class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        seen = set() #(x,y)
        perimeter = 0
        def dfs(x,y):
            nonlocal perimeter
            if ((x,y) in seen) or (x<0) or (y>=col) or (x>=row) or (y<0) or grid[x][y] == 0:
                perimeter += 1
                return 
            seen.add((x,y))
            for dx,dy in direction:
                if (x+dx,y+dy) not in seen:
                    dfs(x+dx,y+dy)


        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    sx,sy = x,y
                    break
        dfs(sx,sy)
                    # break
        return perimeter


        