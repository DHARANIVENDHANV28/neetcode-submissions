class Solution:
    def findLucky(self, arr: List[int]) -> int:

        HashMap = {}

        for n in arr:
            if n not in HashMap:
                HashMap[n] = 0
            HashMap[n] += 1
        
        res = -1
        for k,v in HashMap.items():
            if k == v:
                res = max(res,v)
        
        return res 
        