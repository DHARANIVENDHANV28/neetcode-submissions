class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = len(words)
        for w in words:
            for s in w:
                if s not in set(allowed):
                    res -= 1
                    break
        return res


        