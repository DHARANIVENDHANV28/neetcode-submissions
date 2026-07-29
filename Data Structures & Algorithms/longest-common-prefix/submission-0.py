class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1 = strs[0]

        for s2 in strs[1:]:
            i = 0
            s = ""
            while i<min(len(s1),len(s2)) and s1[i]==s2[i]:
                s += s1[i]
                i += 1
            s1 = s
        
        return s1
        