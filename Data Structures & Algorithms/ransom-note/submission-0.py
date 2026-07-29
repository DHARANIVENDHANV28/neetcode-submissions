class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Ransom = {}
        Magazine = {}

        for c in ransomNote:
            if c not in Ransom:
                Ransom[c] = 1
            else:
                Ransom[c] += 1

        for c in magazine:
            if c not in Magazine:
                Magazine[c] = 1
            else:
                Magazine[c] += 1

        for k,v in Ransom.items():
            if k not in Magazine or Magazine[k] < v:
                return False
        return True
        