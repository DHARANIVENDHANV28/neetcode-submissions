class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        HashMap = {}

        for w in words:
            for c in w:
                if c not in HashMap:
                    HashMap[c] = 0
                HashMap[c] += 1
        
        for k,v in HashMap.items():
            if v % len(words):
                return False
        return True