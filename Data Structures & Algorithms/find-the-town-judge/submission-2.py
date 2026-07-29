class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        HashMap = {k:[] for k in range(1,n+1)}
        if n-1 != len(trust):
            return -1
        for key,val in trust:
            HashMap[key].append(val)
            if len(HashMap[key]) > 1:
                return -1
        for key,val in HashMap.items():
            if HashMap[key] == []:
                return key
        return -1

        