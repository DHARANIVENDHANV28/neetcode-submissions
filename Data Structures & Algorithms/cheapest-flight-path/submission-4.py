class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i:[] for i in range(n)}
        for s,d,c in flights:
            graph[s].append((d,c))
        
        visited = set()
        minHeap = [(0,0,src)]
        res = float('+inf')
        while minHeap:
            # print(minHeap)
            cost,stop,node = heapq.heappop(minHeap)
            # print(c1,path,n1)
            if node==dst:
                return cost
            if stop == k+1:
                continue
            visited.add((node,stop))
            
            for nei,cost2 in graph[node]:
                if (nei,stop+1) not in visited:
                    heapq.heappush(minHeap,(cost+cost2,stop+1,nei))
        return -1
    
            

        