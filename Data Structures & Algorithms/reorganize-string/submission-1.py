class Solution:
    def reorganizeString(self, s: str) -> str:
        HashMap = {}
        outstr = ""
        prev = None
        for c in s:
            if c not in HashMap:
                HashMap[c] = 0
            HashMap[c] += 1
        #[[cnt,char]]
        MaxHeap = [[-1*v,k] for k,v in HashMap.items()]
        heapq.heapify(MaxHeap)
        while MaxHeap or prev:
            if prev and not MaxHeap:
                return ""
            cnt,char = heapq.heappop(MaxHeap)
            outstr += char
            cnt += 1
            if prev:
                heapq.heappush(MaxHeap,prev)
                prev = None
            if cnt < 0:
                prev = [cnt,char]
            
        return outstr 

