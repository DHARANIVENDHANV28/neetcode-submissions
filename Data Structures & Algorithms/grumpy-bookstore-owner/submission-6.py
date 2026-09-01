class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        Satisfied = 0
        notGrump = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                Satisfied += customers[i]
        l = 0
        
        for r in range(len(customers)-minutes+1):
            SUM = 0
            for i in range(minutes):
                if grumpy[r+i] == 1:
                    SUM += customers[r+i]
            notGrump = max(notGrump,SUM)
        
        return Satisfied+notGrump



































        # Total = 0
        # HashMap = {} #idx:customers
        # output = 0
        # for idx in range(len(grumpy)):
        #     if grumpy[idx] == 0:
        #         Total += customers[idx]
        #     else:
        #         HashMap[idx] = customers[idx]

        
        # for j in range(len(grumpy)-minutes+1):
        #     res = Total
        #     for w in range(j,j+minutes):
        #         if w in HashMap:
        #             res = res+HashMap[w]
        #     output = max(res,output)
        # return output
        
