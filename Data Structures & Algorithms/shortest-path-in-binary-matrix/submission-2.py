class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
        ROWS,COLS = len(grid),len(grid)
        res = 1
        visited = set((0,0))
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        q = deque()
        q.append((0,0))
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if (r,c) == (ROWS-1,COLS-1):
                    return res
                for dr,dc in directions:
                    curR,curC = r+dr,c+dc
                    if (curR<0 or curC<0 or curR>=ROWS or curC >=COLS or grid[curR][curC] == 1 or ((curR,curC) in visited)):
                        continue

                    visited.add((curR,curC))
                    q.append((curR,curC))
            res += 1
        return -1

        