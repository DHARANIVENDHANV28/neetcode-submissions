class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        ROWS,COLS = len(picture),len(picture[0])
        res = 0
        row = [False]*ROWS
        col = [False]*COLS
        B = []
        for r in range(ROWS):
            cnt = 0
            for c in range(COLS):
                if picture[r][c] == 'B':
                    B.append([r,c])
                    cnt += 1
            if cnt == 1:
                row[r] = True
        for c in range(COLS):
            cnt = 0
            for r in range(ROWS):
                if picture[r][c] == 'B':
                    cnt += 1
            if cnt == 1:
                col[c] = True
        
        for r,c in B:
            if row[r] == True and col[c] == True:
                res += 1
        return res
            

        
        