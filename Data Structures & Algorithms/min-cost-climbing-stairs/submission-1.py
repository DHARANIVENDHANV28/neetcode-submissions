class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        HashMap = {0:cost[0],1:cost[1]}
        def f(x): 
            if x in HashMap:
                return HashMap[x]
            else:
                HashMap[x] = min(f(x-1),f(x-2))+cost[x]
                return HashMap[x]
        print(HashMap)
        return min(f(len(cost)-1),f(len(cost)-2))
        