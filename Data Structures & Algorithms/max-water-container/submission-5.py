class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights)-1
        while l<=r :
            # print(heights[l],heights[r])
            h = min(heights[l],heights[r])
            w = r-l
            res = max(res,h*w)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return res































        # max_area = 0
        # for i in range(0,len(heights)-1):
        #     for j in range(i+1,len(heights)):
        #         max_area = max(max_area,min(heights[i],heights[j])*(j-i))
        # return max_area