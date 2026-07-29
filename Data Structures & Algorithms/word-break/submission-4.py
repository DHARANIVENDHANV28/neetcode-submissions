class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashmap = {}
        def dfs(i):
            if i==len(s):
                return True
            if i in hashmap:
                return hashmap[i]
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        hashmap[i] = True
                        return hashmap[i]
            hashmap[i] = False 
            return hashmap[i]
        return dfs(0)