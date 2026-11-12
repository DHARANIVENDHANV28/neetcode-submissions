class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u'}
        res = ""
        for ch in s:
            if ch in vowels:
                continue
            res+=ch

        return res
