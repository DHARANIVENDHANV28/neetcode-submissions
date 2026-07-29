class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        seen = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        max_area = 0
        area = 0
        def dfs(r,c):
            nonlocal area
            if (r<0 or c<0 or r>=row or c>=col or grid[r][c] == 0 or (r,c) in seen):
                return 
            area+=1
            seen.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc)
            return area

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in seen:
                    area = dfs(r,c)
                    max_area = max(max_area,area) 
                    area = 0
        return max_area
        