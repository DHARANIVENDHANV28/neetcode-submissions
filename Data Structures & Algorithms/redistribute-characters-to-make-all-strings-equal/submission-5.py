class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        HashMap = {}

        TotalChars = 0
        for w in words:
            TotalChars += len(w)
            for c in w:
                if c not in HashMap:
                    HashMap[c] = 0
                HashMap[c] += 1
        if TotalChars%len(words) != 0:
            return False
        StrSize = TotalChars/len(words)
        VAL = TotalChars/len(HashMap)
        print(TotalChars,VAL,HashMap)

        for k,v in HashMap.items():
            if v != VAL or StrSize < len(HashMap):
                return False
        return True