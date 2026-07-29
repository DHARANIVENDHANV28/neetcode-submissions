class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        HashMap = {}
        s = s.split()
        print(set(pattern),set(s))
        if len(pattern) != len(s) or len(set(pattern)) != len(set(s)):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in HashMap :
                HashMap[pattern[i]] = s[i]
                print(HashMap)
            elif pattern[i] in HashMap and HashMap[pattern[i]] != s[i]:
                return False
        return True 

        