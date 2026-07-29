class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) #O(N)
        while len(stones) > 1: #runs N times therefore T = O(NlogN)
            val1 = -heapq.heappop(stones)  #O(logN)
            val2 = -heapq.heappop(stones)  #O(logN)
            if val1 != val2:
                heapq.heappush(stones,-(val1-val2)) #O(logN)
        return -stones[0] if stones else 0


        # s = stones
        # while len(s) >=2:
        #     s = sorted(s)
        #     val1,val2 = s[-1],s[-2]
        #     s = s[:-2]
        #     if val1 > val2 or val2 > val1:
        #         s.append(abs(val1-val2))
        # return s[0] if s else 0
        