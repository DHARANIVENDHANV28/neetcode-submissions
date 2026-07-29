class Solution:
    def trap(self, height: List[int]) -> int:
        max_L = {}
        max_R = {}
        area = 0
        left,right = 0,0
        for i,l in enumerate(height):
            left = max(left,l)
            max_L[i] = left
        for j,r in enumerate(height[::-1]):
            right = max(right,r)
            max_R[len(height)-j-1] = right
        for idx in range(len(height)):
            A = min(max_L[idx],max_R[idx]) - height[idx]
            if A >=0:
                area += A
        return area

    



        