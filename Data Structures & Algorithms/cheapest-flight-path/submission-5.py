class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i:[] for i in range(n)}
        for s,d,c in flights:
            graph[s].append((d,c))
        
        visited = set()
        minHeap = [(0,0,src)]
        while minHeap:
            cost,stop,node = heapq.heappop(minHeap)
            if node==dst:
                return cost
 
            visited.add((node,stop))
            for nei,cost2 in graph[node]:
                if (nei,stop+1) not in visited and stop+1<=k+1:
                    heapq.heappush(minHeap,(cost+cost2,stop+1,nei))
        return -1
    
            

        