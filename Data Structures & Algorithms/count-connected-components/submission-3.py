class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        HashMap = {i:[] for i in range(n)}
        for n1,n2 in edges:
            HashMap[n1].append(n2)
            HashMap[n2].append(n1)
        visited = set()
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for j in HashMap[node]:
                dfs(j)

        output = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            output+=1
            
        return output
        