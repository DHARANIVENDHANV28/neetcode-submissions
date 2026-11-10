class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        HashMap = {} #char:cnt
        for c in s:
            if c not in HashMap:
                HashMap[c] = 0
            HashMap[c]+=1
        ans = 0
        for c in s:
            if HashMap[c]>0:
                ans+=HashMap[c]
                HashMap[c]-=1
        return ans
