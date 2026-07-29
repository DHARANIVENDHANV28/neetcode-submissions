class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i = False
        j = False
        res = float('+inf')
        for idx,w in enumerate(wordsDict):
            if w == word1:
                i = True
                ival = idx
            if w == word2:
                j = True
                jval = idx
            if i and j:
                res = min(res,abs(ival-jval))
        return res

        