class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        MaxHeap = []
        if a > 0:
            MaxHeap.append([-1*a,"a"])
        if b > 0:
            MaxHeap.append([-1*b,"b"])
        if c > 0:
            MaxHeap.append([-1*c,"c"])
        heapq.heapify(MaxHeap)
        print(MaxHeap)
        
        while MaxHeap:
            cnt,char = heapq.heappop(MaxHeap)
            if len(res) > 1 and res[-1]==res[-2]==char:
                if not MaxHeap:
                    break
                cnt2,char2 = heapq.heappop(MaxHeap)
                res += char2
                cnt2 += 1
                if cnt2<0:
                    heapq.heappush(MaxHeap,[cnt2,char2])
                heapq.heappush(MaxHeap,[cnt,char])
            else:
                res += char
                cnt += 1
                if cnt < 0:
                    heapq.heappush(MaxHeap,[cnt,char])
        return res
        