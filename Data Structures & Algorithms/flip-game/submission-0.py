class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res = []
        n = len(currentState)
        for i in range(n):
            if i+1<n and currentState[i:i+2]=='++':
                adjpairs = '--'
                res.append(currentState[:i]+adjpairs+currentState[i+2:])
                print(currentState[:i]+adjpairs+currentState[i+2:])
        return res
