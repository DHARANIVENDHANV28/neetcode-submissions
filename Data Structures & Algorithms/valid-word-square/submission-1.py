class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        words_c = [""]*len(words)
        for w in words:
            if len(w) > len(words):
                return False
            for i,ch in enumerate(w):
                words_c[i] += ch
        return True if words_c==words else False
        

        