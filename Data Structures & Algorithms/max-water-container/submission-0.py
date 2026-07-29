class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for idx_i,i in enumerate(heights):
            for idx_j,j in enumerate(heights):
                if idx_i != idx_j:
                    width = (idx_j+1)-(idx_i+1)
                    height = min(j,i)
                    print(width,height)
                    area = width*height
                    max_area = max(max_area,area)
        return max_area
        