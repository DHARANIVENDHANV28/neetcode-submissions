class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct,seen = list(), list()
        for s in arr:
            if s in distinct:
                distinct.remove(s)
                seen.append(s)
            elif s not in seen:
                distinct.append(s)
        
        for s in arr:
            if s in distinct:
                k -= 1
                if k == 0:
                    return s
        
        return ""
        