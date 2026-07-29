class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        HashMap = {}

        def dfs(rem):
            if rem in HashMap:
                return HashMap[rem]
            if rem<0:
                return float("inf")
            if rem == 0:
                return 0
            min_coins = float("inf")
            for c in coins:
                min_coins = min(min_coins,dfs(rem-c)+1)
            HashMap[rem] = min_coins
            return min_coins
        result = dfs(amount)
        return result if result != float("inf") else -1


















        # output = float("inf")
        # def dfs(total,cnt):
        #     nonlocal output
        #     if total>amount:
        #         return 
        #     if total == amount:
        #         output = min(output,cnt)
        #         return
        #     for c in sorted(coins,reverse=True):
        #         dfs(c+total,cnt+1)
        # dfs(0,0)
        # return output if output != float("inf") else -1

        