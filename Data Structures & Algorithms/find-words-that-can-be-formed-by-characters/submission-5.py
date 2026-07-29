class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        output = 0
        for w in words:
            HashMap = {}
            for c in chars:
                if c not in HashMap:
                    HashMap[c] = 1
                else:
                    HashMap[c] += 1
            res = 0
            for c in w:
                if c in HashMap and HashMap[c] > 0:
                    HashMap[c] -= 1
                    res += 1
                else:
                    res = 0
                    break
            if res == len(w):
                output += res
        return output
        

