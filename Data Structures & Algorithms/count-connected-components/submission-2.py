class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        HashMap = {i:[] for i in range(n)}
        for n1,n2 in edges:
            HashMap[n1].append(n2)
            HashMap[n2].append(n1)
        print(HashMap)
        visited = set()
        def dfs(node,parent): #->bool
            if node in visited:
                return 
            visited.add(node)
            for j in HashMap[node]:
                if j == parent:
                    continue
                dfs(j,node)
                    # return False
            # return True
        output = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i,-1)
            output+=1
            
        return output
        