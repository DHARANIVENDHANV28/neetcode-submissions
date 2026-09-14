class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        HashMap = {}

        for r in range(n):
            HashMap['R'+str(r)] = []
            for c in range(n):
                if isConnected[r][c] == 1:
                    HashMap['R'+str(r)].append('C'+str(c))
        
        for c in range(n):
            HashMap['C'+str(c)] = []
            for r in range(n):
                if isConnected[r][c] == 1:
                    HashMap['C'+str(c)].append('R'+str(r))
        
        visited = set()
        def bfs(node):
            queue = deque()
            queue.append(node)
            visited.add(node)

            while queue:
                print(visited)
                ele = queue.popleft()
                for l in HashMap[ele]:
                    if l in visited:
                        continue
                    queue.append(l)
                    visited.add(l)
                    
            return 1
        
        res = 0
        for k,v in HashMap.items():
            if k not in visited:
                res+=bfs(k)
        return res



        