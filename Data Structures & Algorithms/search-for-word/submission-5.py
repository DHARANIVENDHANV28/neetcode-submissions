class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set() #{(r,c)}

        ROWS = len(board)
        COLS = len(board[0])
        direction = [[1,0],[0,1],[0,-1],[-1,0]]
    
        def dfs(r, c, idx):

            # Failure base cases
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                board[r][c] != word[idx]):
                return False

            # Success base case
            if idx == len(word) - 1:
                return True

            visited.add((r, c))

            for dr, dc in direction:
                if dfs(r + dr, c + dc, idx + 1):
                    return True

            visited.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False


















































        # ROW = len(board)
        # COL = len(board[0])
        # path = set()
        # def dfs(r,c,i):
        #     if i == len(word):
        #         return True
        #     if (r<0 or r>=ROW or c < 0 or c>=COL or word[i] != board[r][c] 
        #     or (r,c) in path):
        #         return False
        #     path.add((r,c))
        #     res = (dfs(r-1,c,i+1) or
        #           dfs(r+1,c,i+1) or
        #           dfs(r,c-1,i+1) or
        #           dfs(r,c+1,i+1))
        #     path.remove((r,c))
        #     return res


        # for r in range(ROW):
        #     for c in range(COL):
        #         if dfs(r,c,0):
        #             return True
        # return False
        