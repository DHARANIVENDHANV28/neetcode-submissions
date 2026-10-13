class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1,n+1)}
        for s,d,c in times:
            graph[s].append((d,c))
        
        minHeap = [(0,k)]
        visited = set()
        res = 0
        while minHeap:
            cost1,node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res,cost1)
            for nei,cost2 in graph[node]:
                if nei not in visited: 
                    heapq.heappush(minHeap,(cost1+cost2,nei))
        return res if len(visited)==n else -1