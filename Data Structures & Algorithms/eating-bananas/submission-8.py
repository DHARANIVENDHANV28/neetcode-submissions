class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        k_list = []
        while l<=r:
            m = l+((r-l)//2)
            #code for h_val
            h_val = 0
            for val in piles:
                if val % m != 0:
                    if val<=3:
                        h_val+=1
                    else:
                        h_val+=(val//m) + 1
                else:
                    h_val+=val/m
            if h_val<=h:
                k_list.append(m)
                r = m-1
            else:
                l = m+1
        return min(k_list)

        