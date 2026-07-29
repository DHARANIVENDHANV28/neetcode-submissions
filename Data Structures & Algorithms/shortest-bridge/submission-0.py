from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        # DFS to mark first island
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                grid[r][c] == 0 or (r, c) in visited):
                return
            
            visited.add((r, c))  # ✅ FIX
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # BFS to reach second island
        def bfs():
            res = 0
            q = deque(visited)

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dr, dc in directions:  # ✅ FIX
                        curR, curC = r + dr, c + dc

                        if (curR < 0 or curC < 0 or 
                            curR >= ROWS or curC >= COLS or 
                            (curR, curC) in visited):
                            continue

                        if grid[curR][curC] == 1:
                            return res

                        q.append((curR, curC))
                        visited.add((curR, curC))

                res += 1

        # Find first island
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()