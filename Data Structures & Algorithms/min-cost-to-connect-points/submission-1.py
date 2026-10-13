class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {tuple(i):[] for i in points}
        for p1 in points:
            for p2 in points:
                if p1 == p2:
                    continue
                cost = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
                graph[tuple(p1)].append((p2,cost))
        # print(graph)
        #[([x,y],cost)]
        def dijkstra(start):
            minHeap = [(0,tuple(start))]
            visited = set()
            # visited.add(tuple(points[0]))
            res = 0
            while minHeap:
                c,p = heapq.heappop(minHeap)
                # print(p,c)
                if p in visited:
                    continue
                visited.add(p)
                res+=c
                for nei in graph[p]:
                    if tuple(nei[0]) not in visited:
                        heapq.heappush(minHeap,(nei[1],tuple(nei[0])))
                        # visited.add(tuple(nei[0]))
            return res
        return dijkstra(points[0])
        