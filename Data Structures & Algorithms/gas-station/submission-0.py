class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for start in range(n):
            if gas[start] >= cost[start]:
                G = gas[start:n+1]+gas[0:start+1]
                C = cost[start:n+1]+cost[0:start+1]
                print(G,C)
                tracker = 0
                for idx in range(n+1):
                    print("tracker",tracker)
                    tracker += 1
                    if idx == 0:
                        tank = G[idx]
                    else:
                        tank = tank+G[idx]-C[idx-1]
                    print("tank",tank)
                    if tank < 0 or tank < C[idx]:
                        break
                if tracker == n+1:
                    return start
        return -1
                
        