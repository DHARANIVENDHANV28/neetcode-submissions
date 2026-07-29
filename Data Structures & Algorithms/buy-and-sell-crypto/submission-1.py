class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        i = 0
        j = 1
        while j < (len(prices)):
            print(i,j)
            if prices[i] > prices[j]:
                i += 1
                j = i+1
            if j < len(prices):
                if prices[i] <= prices[j] :
                    profit = prices[j] - prices[i]
                    max_p = max(max_p,profit)
                    j += 1
        return max_p
        
        


        