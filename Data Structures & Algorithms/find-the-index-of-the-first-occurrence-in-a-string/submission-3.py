class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        res = ""
        for r in range(len(haystack)):
            res+=haystack[r]
            if len(res)>len(needle):
                res = res[1:]
                l+=1
        
            if res == needle:
                return l
            
        return -1
            
        