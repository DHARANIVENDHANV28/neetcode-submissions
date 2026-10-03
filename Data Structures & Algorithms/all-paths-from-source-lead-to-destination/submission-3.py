class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = {i:[] for i in range(n)}
        for n1,n2 in edges:
            graph[n1].append(n2)
        visited = set()
        def dfs(node): #bool
            #bc
            if node in visited: #cycle detected
                return False
            if graph[node] == [] and node != destination:
                return False
            if graph[node] == [] and node == destination:
                return True

            visited.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited.remove(node)
            return True
        
        return dfs(source)
        