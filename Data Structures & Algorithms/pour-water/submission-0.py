class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        res = heights.copy()
        for v in range(volume):
            pos = k
            for l in range(k-1,-1,-1):
                if res[l]>res[l+1]:
                    break
                if res[l]<res[pos]:
                    pos=l
            if pos!=k:
                res[pos]+=1
                continue
            pos = k
            for r in range(k+1,len(heights)):
                if res[r]>res[r-1]:
                    break
                if res[r]<res[pos]:
                    pos = r
                    
            res[pos]+=1
                 
        return res
