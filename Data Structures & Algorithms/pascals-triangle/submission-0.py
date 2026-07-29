class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        if numRows == 1:
            return output
        for r in range(2,numRows+1):
            pascal_row = []
            for idx in range(0,r):
                arr = [0]+output[-1]+[0]
                pascal_row.append(arr[idx]+arr[idx+1])
                print(arr,pascal_row)
            output.append(pascal_row)
        return output

        