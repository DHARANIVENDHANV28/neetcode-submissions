# class Solution:
#     def numEnclaves(self, grid: List[List[int]]) -> int:
#         ROWS = len(grid)
#         COLS = len(grid[0])

#         directions = [[1,0],[0,1],[-1,0],[0,-1]]

#         def dfs(r,c):
#             if (r<0) or (c<0) or (r>=ROWS) or (c>=COLS) or ((r,c) in visited) or (grid[r][c] == 0):
#                 return 
#             if (r==0) or (r==ROWS-1) or (c==0) or (c==COLS-1):
#                 return True
#             visited.add((r,c))
#             for dr,dc in directions:
#                 if dfs(r+dr,c+dc):
#                     return True
#             return False

#         Output = 0
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == 1:
#                     visited = set()
#                     if not dfs(r,c):
#                         Output+=1
#         return Output
class Solution:
    def numEnclaves(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return
            grid[r][c] = 0  # mark as visited (remove land)
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Step 1: Remove all boundary-connected land
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS - 1] or c in [0, COLS - 1]) and grid[r][c] == 1:
                    dfs(r, c)

        # Step 2: Count remaining land (enclaves)
        enclaves = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    enclaves += 1

        return enclaves