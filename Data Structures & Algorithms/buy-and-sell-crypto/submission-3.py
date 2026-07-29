class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        j = i+1
        while i<j and j < len(prices):
            print(i,j)
            profit = max(profit,prices[j]-prices[i])
            if j == len(prices)-1:
                i+=1
                j=i+1
            else:
                j+=1
        return profit
        