class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        Dir = 1
        curRow = 0
        rows = ['']*numRows
        # print(rows)
        for i,ch in enumerate(s):
            rows[curRow] += ch
            # print(curRow)
            if curRow == 0:
                Dir = 1
            elif curRow == numRows-1:
                Dir = -1
            curRow += Dir
        return "".join(rows)

        # LEN,i = 0,0
        # HashMap = {}
        # while LEN < len(s):
        #     while i < numRows and LEN < len(s):
        #         if i not in HashMap:
        #             HashMap[i] = []
        #         HashMap[i] += s[LEN]
        #         i+=1
        #         LEN+=1
        #     i-=1
        #     while i != 0 and LEN < len(s):
        #         i-=1
        #         if i not in HashMap:
        #             HashMap[i] = []
        #         HashMap[i] += s[LEN]
        #         LEN+=1
        #     i+=1
        # res = ""
        # for i in range(numRows):
        #     if i not in HashMap:
        #         break
        #     res += "".join(HashMap[i])
        # return res