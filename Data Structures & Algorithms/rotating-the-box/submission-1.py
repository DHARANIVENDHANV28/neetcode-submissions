class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS,COLS = len(boxGrid),len(boxGrid[0])
        output = []
        # print(output)

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if boxGrid[r][c] == ".":
        #             curC= c
        #             while curC>=0 and boxGrid[r][curC-1] == "#":
        #                 boxGrid[r][curC-1],boxGrid[r][curC] = ".","#"
        #                 curC -= 1
        
        for c in range(COLS):
            for r in range(ROWS):
                res = [boxGrid[r][c] for r in range(ROWS)]
            output.append(res[::-1])
        print(output)
        

        for c in range(len(output[0])):
            for r in range(len(output)):
                if output[r][c] == ".":
                    curR = r
                    while curR>0 and output[curR-1][c] == "#":
                        output[curR][c],output[curR-1][c] = "#","."
                        curR -= 1
        return output
        
                
        