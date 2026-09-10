class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        # res = []

        # def dfs(num,start,sub):
        #     if num == 1:
        #         res.append(sub.copy())
        #         return None
        #     for i in range(start,num):
        #         if num%i != 0:
        #             continue
        #         sub.append(i)
        #         dfs(num//i,i,sub)
        #         sub.pop()
        #     if start == num:
        #         sub.append(num)
        #         dfs(1,num,sub)
        #         sub.pop()
        #     return None
        
        # dfs(n,2,[])
        
        # return res



























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
        