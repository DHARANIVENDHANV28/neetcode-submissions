class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        q = deque()
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(rows):
            for c in range(cols):
                if r in [0,rows-1] and board[r][c] == "O":
                    q.append([r,c])
                    visited.add((r,c))
                if r not in [0,rows-1] and c in [0,cols-1] and board[r][c] == "O":
                    q.append([r,c])
                    visited.add((r,c))

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row = r+dr
                    col = c+dc
                    if row<rows and col<cols and row>=0 and col>=0 and board[row][col] != "X" and (row,col) not in visited:
                        visited.add((row,col))
                        q.append([row,col])

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited:
                    board[r][c] = 'X'




        




        