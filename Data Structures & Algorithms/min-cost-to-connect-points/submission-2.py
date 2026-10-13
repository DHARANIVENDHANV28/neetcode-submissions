class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {tuple(i):[] for i in points}
        for p1 in points:
            for p2 in points:
                if p1 == p2:
                    continue
                cost = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
                graph[tuple(p1)].append((p2,cost))

        def prims(start):
            minHeap = [(0,tuple(start))]
            visited = set()
            res = 0
            while minHeap:
                c,p = heapq.heappop(minHeap)
                if p in visited:
                    continue
                visited.add(p)
                res+=c
                for nei in graph[p]:
                    if tuple(nei[0]) not in visited:
                        heapq.heappush(minHeap,(nei[1],tuple(nei[0])))
            return res
        return prims(points[0])
        