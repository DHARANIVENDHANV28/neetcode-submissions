class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        res = 0
        def dfs(nbottles):
            nonlocal res
            #bc
            if nbottles<numExchange:
                res+=nbottles
                return None
            res+=numExchange
            dfs(nbottles-numExchange+1)
            return None
        
        dfs(numBottles)
        return res

