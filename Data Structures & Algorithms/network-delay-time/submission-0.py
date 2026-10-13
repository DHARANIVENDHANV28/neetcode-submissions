class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1,n+1)}
        for s,d,c in times:
            graph[s].append((d,c))
        print(graph)
        
        minHeap = [(0,k)]
        HashMap = {}
        visited = set()
        visited.add(k)
        res = 0
        while minHeap:
            print(minHeap)
            cost1,node = heapq.heappop(minHeap)
            if node in HashMap:
                continue
            HashMap[node] = cost1
            visited.add(node)
            res = max(res,cost1)
            for nei,cost2 in graph[node]:
                if nei not in HashMap:
                    
                    heapq.heappush(minHeap,(cost1+cost2,nei))
        print(HashMap)
        return res if len(HashMap)==n else -1