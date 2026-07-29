class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap_s = {}
        hashmap_t = {}
        if t == "":
            return ""
        for c in t:
            if c not in hashmap_t:
                hashmap_t[c] = 1
            else:
                hashmap_t[c]+=1
        l = 0
        have,need = 0,len(hashmap_t)
        res,resLen = [-1,-1],float("infinity")
        
        for r in range(0,len(s)):
            if s[r] not in hashmap_s:
                hashmap_s[s[r]] = 1
            else:
                hashmap_s[s[r]] += 1
            if s[r] in hashmap_t and hashmap_s[s[r]] == hashmap_t[s[r]]:
                have+=1
            while have==need:
                if resLen>(r-l+1):
                    res = [l,r]
                    resLen = min(resLen,r-l+1)
                hashmap_s[s[l]] -= 1
                if s[l] in hashmap_t and hashmap_s[s[l]] < hashmap_t[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""

