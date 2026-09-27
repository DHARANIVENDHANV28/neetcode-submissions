class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = {i:[] for i in range(n)}
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        # print(graph)

        def bfs(root): #return height
            visited = set()
            queue = deque()
            queue.append(root)
            visited.add(root)
            height = -1

            while queue:
                height+=1
                for _ in range(len(queue)):
                    node = queue.popleft()   
                    for nei in graph[node]:
                        if nei in visited:
                            continue
                        visited.add(nei)
                        queue.append(nei)

            return height

        reshas = {i:[] for i in range(n)}
        for rn in range(n):
            h = bfs(rn)
            # print(rn,h)
            reshas[h].append(rn)
        for i in range(n):
            if reshas[i]!=[]:
                return reshas[i]
        
        