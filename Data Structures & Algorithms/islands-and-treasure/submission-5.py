class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        INF = 2147483647

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c,0])
        while q:
            for i in range(len(q)):
                r,c,dist = q.popleft()
                for dr,dc in directions:
                    distance = dist
                    row = r+dr
                    col = c+dc
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == INF:
                        distance += 1
                        q.append([row,col,distance])
                        grid[row][col] = grid[r][c]+1  
            



        