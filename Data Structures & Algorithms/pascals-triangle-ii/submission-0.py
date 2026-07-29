class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        
        pascal = [[1,1]]

        for r in range(1,rowIndex):
            res = []
            lastele = pascal[-1]
            for i in range(0,len(lastele)-1):
                res.append(lastele[i]+lastele[i+1])
            pascal.append([1]+res+[1])
            print(pascal)
        
        return pascal[-1]
        