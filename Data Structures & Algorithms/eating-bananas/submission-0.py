class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L,R = 1,max(piles)
        result = R

        while L<=R:
            M = L+(R-L)//2
            time = 0
            for p in piles:
                time += math.ceil(float(p)/M)
            if time <= h:
                result = M
                R = M-1
            else:
                L = M+1
        return result
            

            