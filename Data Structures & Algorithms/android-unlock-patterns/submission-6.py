class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:

        res = 0
        skip = [[0]*9 for _ in range(9)]
        skip[0][2] = skip[2][0] = 1
        skip[0][6] = skip[6][0] = 3
        skip[2][8] = skip[8][2] = 5
        skip[6][8] = skip[8][6] = 7

        skip[0][8] = skip[8][0] = 4
        skip[2][6] = skip[6][2] = 4

        skip[1][7] = skip[7][1] = 4
        skip[3][5] = skip[5][3] = 4

        
        def dfs(node,l):
            nonlocal res
            if l>n:
                return None

            visited.add(node)

            if m<=l<=n:
                res+=1
            
            for nxt in range(9):
                if nxt in visited:
                    continue
                if skip[node][nxt] == 0 or skip[node][nxt] in visited:
                    dfs(nxt,l+1)

            visited.remove(node)
            return None


        visited = set()
        for node in range(0,9):
                dfs(node,1)
        return res





































































        # visited = set()
        # skip = [[0]*10 for _ in range(0,10)]
        # skip[1][3] = skip[3][1] = 2
        # skip[1][7] = skip[7][1] = 4
        # skip[1][9] = skip[9][1] = 5
        # skip[2][8] = skip[8][2] = 5
        # skip[3][9] = skip[9][3] = 6
        # skip[4][6] = skip[6][4] = 5
        # skip[7][9] = skip[9][7] = 8
        # skip[3][7] = skip[7][3] = 5

        # def dfs(cur,npins): #return res
        #     res = 0
        #     #BaseCase
        #     if  npins>n:
        #         return 0
        #     if npins>=m:
        #         res += 1
        #     for nxt in range(1,10):
        #         if nxt in visited:
        #             continue
        #         if skip[cur][nxt] != 0 and skip[cur][nxt] not in visited:
        #             continue
        #         visited.add(nxt)
        #         res+=dfs(nxt,npins+1)
        #         visited.remove(nxt)
        #     return res

        # res = 0
        # for start in range(1,10):
        #     visited.add(start)
        #     res+=dfs(start,1)
        #     visited.remove(start)
        # return res
        