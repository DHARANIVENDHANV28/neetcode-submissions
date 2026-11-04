class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cTime = 0
        SUM = 0
        for arrival, prep in customers:
            if cTime<=arrival:
                cTime = arrival
            cTime += prep
            SUM += (cTime-arrival)
        return SUM/len(customers)

        