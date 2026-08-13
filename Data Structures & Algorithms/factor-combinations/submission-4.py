class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        if n<2:
            return res

        def dfs(num,fact,arr):
            if fact == 1:
                res.append(arr.copy())
                return None
            for i in range(num,int(math.sqrt(fact))+1):
                if fact%i == 0:
                    arr.append(i)
                    dfs(i,fact//i,arr)
                    arr.pop()
            if fact>=num and fact != n:
                arr.append(fact)
                dfs(fact,1,arr)
                arr.pop()
        
        dfs(2,n,[])
        return res
        