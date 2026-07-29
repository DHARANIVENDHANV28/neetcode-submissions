class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        OUT = defaultdict(int)
        IN = defaultdict(int)

        for src,dst in trust:
            OUT[src] += 1
            IN[dst] += 1

        for i in range(1,n+1):
            if OUT[i] == 0 and IN[i] == n-1:
                return i
        return -1
