class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0])-1
        ele = 0

        while ele<len(matrix) and l<=r:
            print("ele",ele)
            if target>=matrix[ele][l] and target <= matrix[ele][r]:
                nums = matrix[ele]
                m = l+(r-l)//2
                print('m',m)
                if nums[m]==target:
                    return True
                if nums[m]>target:
                    r = m-1
                if nums[m]<target:
                    l = m+1
            else:
                ele += 1
        return False


        