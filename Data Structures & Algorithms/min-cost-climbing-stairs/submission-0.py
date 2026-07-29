class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        output = []
        def BT(idx,total):
            if idx>=len(cost):
                output.append(total)
                return
            BT(idx+1,total+cost[idx])
            BT(idx+2,total+cost[idx])
        BT(0,0)
        BT(1,0)
        return min(output)
        