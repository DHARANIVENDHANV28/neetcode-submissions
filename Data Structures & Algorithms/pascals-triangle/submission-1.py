class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        if numRows == 1:
            return output
        for r in range(2,numRows+1):
            pascal_row = []
            arr = [0]+output[-1]+[0]
            for idx in range(0,r):
                pascal_row.append(arr[idx]+arr[idx+1])
            output.append(pascal_row)
        return output

        