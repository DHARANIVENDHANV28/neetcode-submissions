class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        visited = set()
        distance = float('+inf')
        ROWS,COLS = len(maze),len(maze[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        def dfs(r,c,d):
            nonlocal distance
            if [r,c] == destination:
                distance = min(d,distance)
                return None
            visited.add((r,c))
            for dr,dc in directions:
                row,col = r,c
                step = 0
                while 0<=row+dr<ROWS and 0<=col+dc<COLS and maze[row+dr][col+dc]==0:
                    row+=dr
                    col+=dc
                    step+=1
                if step>0 and (row,col) not in visited:
                    dfs(row,col,d+step)
            visited.remove((r,c))
            return None
        
        dfs(start[0],start[1],0)
        return distance if distance != float('+inf') else -1


        