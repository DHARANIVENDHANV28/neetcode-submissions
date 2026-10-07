class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited =set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            island = []
            while queue:
                row,col = queue.popleft()
                island.append((row-r,col-c))
                for dr,dc in directions:
                    if row+dr<0 or col+dc<0 or row+dr>=ROWS or col+dc>=COLS or grid[row+dr][col+dc] == 0 or (row+dr,col+dc) in visited:
                        continue
                    queue.append((row+dr,col+dc))
                    visited.add((row+dr,col+dc))
            return tuple(island)

        
        ROWS,COLS = len(grid),len(grid[0])
        res = set()
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visited or grid[r][c]==0:
                    continue
                res.add(bfs(r,c))
                
        return len(res)

        