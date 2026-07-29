class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math
        Gift = [-g for g in gifts]
        heapq.heapify(Gift)

        while k>0:
            Max = -1*(heapq.heappop(Gift))
            heapq.heappush(Gift,(-1*(math.floor(Max**0.5))))
            # print(Gift)
            k-=1
        return int(sum(Gift))*-1
        