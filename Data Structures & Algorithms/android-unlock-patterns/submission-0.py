class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        visited = set()
        skip = [[0]*10 for _ in range(0,10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[1][9] = skip[9][1] = 5
        skip[2][8] = skip[8][2] = 5
        skip[3][9] = skip[9][3] = 6
        skip[4][6] = skip[6][4] = 5
        skip[7][9] = skip[9][7] = 8
        skip[3][7] = skip[7][3] = 5

        def dfs(cur,npins): #return res
            res = 0
            #BaseCase
            if  npins>n:
                return 0
            if npins>=m:
                res += 1
            for nxt in range(1,10):
                if nxt in visited:
                    continue
                if skip[cur][nxt] != 0 and skip[cur][nxt] not in visited:
                    continue
                visited.add(nxt)
                res+=dfs(nxt,npins+1)
                visited.remove(nxt)
            return res

        res = 0
        for start in range(1,10):
            visited.add(start)
            res+=dfs(start,1)
            visited.remove(start)
        return res
        