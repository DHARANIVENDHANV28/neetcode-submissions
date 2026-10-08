class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
        x, y = abs(x), abs(y)
        visited = set()
        def bfs(r,c):
            res = -1
            queue = deque()
            queue.append([0,0])
            visited.add((0,0))
            while queue:
                res+=1
                for _ in range(len(queue)):
                    row,col = queue.popleft()
                    if row == x and col == y:
                        return res
        
                    for dr,dc in directions:
                        nr, nc = row + dr, col + dc
                        if (nr, nc) in visited or nr < -1 or nc < -1:
                            continue
                        visited.add((nr, nc))
                        queue.append([nr, nc])
            return res

        return bfs(0,0)
