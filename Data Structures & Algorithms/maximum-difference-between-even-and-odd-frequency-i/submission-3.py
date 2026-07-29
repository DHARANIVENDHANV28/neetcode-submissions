class Solution:
    def maxDifference(self, s: str) -> int:
        HashMap = {}

        for c in s:
            if c not in HashMap:
                HashMap[c] = 1
            else:
                HashMap[c] += 1
        mineven = float("inf")
        maxodd = float("-inf")
        for k,v in HashMap.items():
            if v % 2 == 0:
                mineven = min(mineven,v)
            else:
                maxodd = max(maxodd,v)
        print(HashMap,maxodd,mineven)
        return maxodd-mineven
        