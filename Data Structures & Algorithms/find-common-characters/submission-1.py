class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word = words[0]
        HashMap = {}
        for w in word:
            if w not in HashMap:
                HashMap[w] = 0
            HashMap[w] += 1
        
        for w in words[1:]:
            hm = {}
            for c in w:
                if c in HashMap:
                    if c not in hm:
                        hm[c] = 0
                    hm[c] += 1
            
            for k,v in HashMap.items():
                if k in hm:
                    HashMap[k] = min(v,hm[k])
                else:
                    HashMap[k] = 0
        res = []
        for k,v in HashMap.items():
            while v != 0:
                res.append(k)
                v -= 1
        return res
                
        