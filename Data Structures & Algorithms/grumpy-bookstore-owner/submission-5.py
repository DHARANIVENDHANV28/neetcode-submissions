class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        Total = 0
        HashMap = {} #idx:customers
        output = 0
        for idx in range(len(grumpy)):
            if grumpy[idx] == 0:
                Total += customers[idx]
            else:
                HashMap[idx] = customers[idx]

        # print(HashMap,Total)
        
        for j in range(len(grumpy)-minutes+1):
            res = Total
            for w in range(j,j+minutes):
                # print(j,w)
                if w in HashMap:
                    res = res+HashMap[w]
                    # print(res,HashMap[w],j,w)
            output = max(res,output)
        return output
        
