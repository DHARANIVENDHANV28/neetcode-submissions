class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]
        ROWS,COLS = len(img),len(img[0])

        res = [[0]*COLS for _ in range(ROWS)]
        # print(res)
        
        for r in range(ROWS):
            for c in range(COLS):
                numofele = 1
                SUM = img[r][c]
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS:
                        continue
                    numofele += 1
                    SUM += img[nr][nc]
                res[r][c] = SUM//numofele
        return res


