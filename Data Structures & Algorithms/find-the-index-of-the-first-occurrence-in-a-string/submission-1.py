class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        res = []
        for r in range(len(haystack)):
            res.append(haystack[r])
            if len(res)>len(needle):
                res.pop(0)
                l+=1
            if len(res) == len(needle):
                if "".join(res) == needle:
                    return l
            
        return -1
            
        