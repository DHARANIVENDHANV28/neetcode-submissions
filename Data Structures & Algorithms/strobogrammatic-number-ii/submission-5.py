class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        res = []
        path = ['']*n
        pairs = [('0','0'),('1','1'),('6','9'),('8','8'),('9','6')]
        def dfs(left,right):
            if left>right:
                res.append("".join(path))
                return None
            for i,j in pairs:
                if left == 0 and n>1 and i == '0':
                    continue
                if left == right and i!=j:
                    continue
                path[left] = i
                path[right] = j
                dfs(left+1,right-1)
                path[left] = ""
                path[right] = ""
            return None
        dfs(0,n-1)
        return res