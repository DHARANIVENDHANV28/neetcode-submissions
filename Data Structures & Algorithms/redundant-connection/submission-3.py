class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(1,len(edges)+1)}
        

        def bfs(start,target):
            visited = set()
            queue = deque()
            queue.append(start)
            visited.add(start)

            while queue:
                node = queue.popleft()
                if node == target:
                    return True
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            return False
        res = []
        for u,v in edges:
            if bfs(u,v):
                res = [u,v]
            else:
                graph[u].append(v)
                graph[v].append(u)
        
        return res



























        # HashMap = {i+1:[] for i in range(len(edges))}
        # for n1,n2 in edges:
        #     HashMap[n1].append(n2)
        #     HashMap[n2].append(n1)
        # visited = set()
        # def dfs(node,prev):
        #     if node in visited:
        #         return 
        #     visited.add(node)
        #     f


        # for n1,n2 in edges:
        #     dfs(n1)
        