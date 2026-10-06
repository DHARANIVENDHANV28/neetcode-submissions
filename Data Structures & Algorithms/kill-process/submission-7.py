class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = {}
        for i in range(len(ppid)):
            if ppid[i] not in graph:
                graph[ppid[i]] = []
            graph[ppid[i]].append(pid[i])
        # print(graph)
        visited = set()
        def bfs(n):
            queue = deque()
            queue.append(n)
            visited.add(n)
            res = []
            while queue:
                node =  queue.popleft()
                res.append(node)
                for nei in graph.get(node,[]):
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            return res

        return bfs(kill)
        
        