class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxWidth = 0
        points = sorted(points)

        for i in range(len(points)-1):
            maxWidth = max(maxWidth,points[i+1][0]-points[i][0])
        return maxWidth
            
            
            
