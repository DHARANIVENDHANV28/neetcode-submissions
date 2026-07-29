class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        def helper(s,t):
            HashMap = {}
            for i in range(len(s)):
                if s[i] in HashMap: 
                    if t[i] != HashMap[s[i]]:
                        return False
                else:
                    HashMap[s[i]] = t[i]
                
            return True
        return helper(s,t) and helper(t,s)


        