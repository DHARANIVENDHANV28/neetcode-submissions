class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}":"{","]":"[",")":"("}
        Lis = []
        if len(s)%2 != 0:
            return False

        for p in s:
            if p in hashmap and len(Lis) != 0 and hashmap[p] == Lis[-1]:
                Lis.pop()
            else:
                Lis.append(p)
        return True if len(Lis) == 0 else False

        
        