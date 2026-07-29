class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = []
        seen = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c,0])
        while q:
            for i in range(len(q)):
                r,c,dist = q.pop(0)
                for dr,dc in directions:
                    distance = dist
                    row = r+dr
                    col = c+dc
                    if (row<0 or col<0 or row>=rows or col>=cols or grid[row][col] == 0 or grid[row][col] == -1 or (row,col) in seen):
                        continue 
                    distance += 1
                    q.append([row,col,distance])
                    seen.add((row,col))
                    grid[row][col] = min(grid[row][col],distance)  
        



        