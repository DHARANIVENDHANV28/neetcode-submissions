class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        HashMap = {}
        for i,k in enumerate(keyboard):
            if k not in HashMap:
                HashMap[k] = 0
            HashMap[k] += i
        
        cur = 0
        res = 0
        for w in word:
            res += abs(HashMap[w]-cur)
            cur = HashMap[w]
        
        return res

        