class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = [] #(idx,height)
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                idx,height = stack.pop()
                area = max(area,height*(i-idx))
                start = idx
            stack.append((start,h))
        for i,h in stack:
            area = max(area,h*(len(heights)-i))
        return area
                

















        # area = 0
        # for j,h in enumerate(heights):
        #     width = 1
        #     for i in range(j-1,-1,-1):
        #         if heights[i]>=h:
        #             width+=1
        #         else:
        #             break
        #     for k in range(j+1,len(heights)):
        #         if heights[k]>=h:
        #             width+=1
        #         else:
        #             break
        #     height = h
        #     A = width*height
        #     area = max(A,area)
        # return area

        