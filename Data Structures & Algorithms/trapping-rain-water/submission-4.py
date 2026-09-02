class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0
        maxL = {}#idx:maxleft
        maxR = {}#idx:maxright
        left,right = 0,0
        for i,l in enumerate(height):
            left = max(left,l)
            maxL[i] = left
        
        for j,r in enumerate(height[::-1]):
            right = max(right,r)
            maxR[len(height)-j-1] = right

        # print(maxR,maxL)

        for i in range(len(height)):
            
            res += (min(maxR[i],maxL[i])-height[i])

        return res 










































        # max_L = {}
        # max_R = {}
        # area = 0
        # left,right = 0,0
        # for i,l in enumerate(height):
        #     left = max(left,l)
        #     max_L[i] = left
        # for j,r in enumerate(height[::-1]):
        #     right = max(right,r)
        #     max_R[len(height)-j-1] = right
        # for idx in range(len(height)):
        #     A = min(max_L[idx],max_R[idx]) - height[idx]
        #     if A >=0:
        #         area += A
        # return area

    



        