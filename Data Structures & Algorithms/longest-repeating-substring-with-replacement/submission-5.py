class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l=0
        length = 0
        max_f = 0 
        for r in range(len(s)):
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
            else:
                hashmap[s[r]] += 1
            max_f = max(max_f,hashmap[s[r]])
            valid = (r-l+1) - max_f
            if valid > k:
                hashmap[s[l]] -= 1
                l+=1
            length = max(length,r-l+1)
        return length