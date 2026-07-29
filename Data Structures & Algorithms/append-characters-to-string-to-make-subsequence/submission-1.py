class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j = 0,0
        output = len(t)
        while i<len(s) and j<len(t) :
            if s[i]==t[j]:
                output -= 1
                i+=1
                j+=1
            else:
                i+=1
            
        return output

        
        