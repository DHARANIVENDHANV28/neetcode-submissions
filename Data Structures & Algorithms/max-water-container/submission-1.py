class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_area = 0

        # for idx_i,i in enumerate(heights):
        #     for idx_j,j in enumerate(heights):
        #         if idx_i != idx_j:
        #             width = (idx_j+1)-(idx_i+1)
        #             height = min(j,i)
        #             print(width,height)
        #             area = width*height
        #             max_area = max(max_area,area)
        # return max_area
        
        right = len(heights)-1
        left = 0
        max_area = 0
        while left<right:
            width = right-left
            height = min(heights[left],heights[right])
            area = width*height
            print(area)
            max_area = max(max_area,area)

            if heights[left]<heights[right]:
                left += 1
            else:
                right -= 1

            max_area = max(max_area,area)
        return max_area
