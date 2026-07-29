class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        HashMap = defaultdict(set)
        if len(sentence1) != len(sentence2):
            return False
        for w in similarPairs:
            w1,w2 = w

            HashMap[w1].add(w2)
            HashMap[w2].add(w1)
        
        print(HashMap)

        for i in range(len(sentence1)):
            if (sentence1[i] == sentence2[i]) or (sentence2[i] in HashMap[sentence1[i]]) :
                continue
            
            return False
            
        return True
