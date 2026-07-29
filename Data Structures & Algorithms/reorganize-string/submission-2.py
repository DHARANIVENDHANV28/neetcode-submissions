class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        HashMap = {}
        for c in s:
            if c not in HashMap:
                HashMap[c] = 0
            HashMap[c] += 1
        
        MaxHeap = [[-1*v,k] for k,v in HashMap.items()] #[[cnt,char]]
        heapq.heapify(MaxHeap)

        while MaxHeap:
            cnt,char = heapq.heappop(MaxHeap)
            if len(res) > 0 and res[-1] == char:
                if not MaxHeap:
                    break
                cnt2,char2 = heapq.heappop(MaxHeap)
                cnt2 += 1
                res += char2
                if cnt2 < 0:
                    heapq.heappush(MaxHeap,[cnt2,char2])
                heapq.heappush(MaxHeap,[cnt,char])
            else:
                res += char
                cnt += 1
                if cnt < 0:
                    heapq.heappush(MaxHeap,[cnt,char])
        
        return res if len(res) == len(s) else ""

















        # HashMap = {}
        # outstr = ""
        # prev = None
        # for c in s:
        #     if c not in HashMap:
        #         HashMap[c] = 0
        #     HashMap[c] += 1
        # #[[cnt,char]]
        # MaxHeap = [[-1*v,k] for k,v in HashMap.items()]
        # heapq.heapify(MaxHeap)
        # while MaxHeap or prev:
        #     if prev and not MaxHeap:
        #         return ""
        #     cnt,char = heapq.heappop(MaxHeap)
        #     outstr += char
        #     cnt += 1
        #     if prev:
        #         heapq.heappush(MaxHeap,prev)
        #         prev = None
        #     if cnt < 0:
        #         prev = [cnt,char]
            
        # return outstr 

