class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        sem = 0
        indeg = {i:0 for i in range(1,n+1)}
        graph = {i:[] for i in range(1,n+1)}
        for prev,cur in relations:
            indeg[cur]+=1
            graph[prev].append(cur)

        def bfs():
            queue = deque()
            for ns in range(1,n+1):
                if indeg[ns] == 0:
                    queue.append(ns)
            semester,courses = 0,0
            while queue:
                semester+=1
                for _ in range(len(queue)):
                    node = queue.popleft()
                    courses += 1
                    for nei in graph[node]:
                        indeg[nei] -= 1
                        if indeg[nei] == 0:
                            queue.append(nei)
            return semester if courses == n else -1
        return bfs()

        