class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        HashMap = {} #char:cnt
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] not in HashMap:
                HashMap[s[r]] = 0
            HashMap[s[r]] += 1
            while len(HashMap)>2:
                HashMap[s[l]] -= 1
                if HashMap[s[l]] == 0:
                    HashMap.pop(s[l])
                l+=1
            res = max(res,r-l+1)
        return res