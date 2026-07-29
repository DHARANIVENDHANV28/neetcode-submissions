class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p = 0
        i = 0

        while i<len(abbr):
            if abbr[i].isdigit():
                if abbr[i] == '0':
                    return False
                num = 0
                while i<len(abbr) and abbr[i].isdigit():
                    num = num*10+int(abbr[i])
                    i+=1
                p+=num
            
            else:
                if p>=len(word) or word[p]!=abbr[i]:
                    return False
                p+=1
                i+=1
        return p==len(word)