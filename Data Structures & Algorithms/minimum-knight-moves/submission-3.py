class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]

        visited = set()
        def bfs(r,c):
            res = -1
            queue = deque()
            queue.append([0,0])
            visited.add((0,0))
            while queue:
                # print(queue)
                res+=1
                for _ in range(len(queue)):
                    row,col = queue.popleft()
                    if row == abs(x) and col == abs(y):
                        return res
        
                    for dr,dc in directions:
                        if (row+dr,col+dc) in visited:
                            continue
                        visited.add((row+dr,col+dc))
                        queue.append([row+dr,col+dc])
            return res

        return bfs(0,0)
        