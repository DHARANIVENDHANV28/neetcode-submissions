class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        visited = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS,COLS = len(maze),len(maze[0])
        def dfs(r,c):
            print(r,c)
            #bc
            if [r,c] == destination:
                return True
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in visited or maze[r][c] == 1:
                return False
            visited.add((r,c))
            for dr,dc in directions:
                row,col = r,c
                while row+dr>=0 and col+dc>=0 and row+dr<ROWS and col+dc<COLS and maze[row+dr][col+dc]==0:
                    row+=dr
                    col+=dc
                if dfs(row,col):
                    return True
            visited.remove((r,c))
            return False
                
        
        return dfs(start[0],start[1])
        