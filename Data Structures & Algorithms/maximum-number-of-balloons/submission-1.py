class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        HashMap = {"b":0,"a":0,"l":0,"o":0,"n":0}
        res = 0
        for s in text:
            if s in HashMap:
                HashMap[s] += 1
            if ((HashMap["b"] >= 1) and (HashMap["a"] >= 1) and (HashMap["l"] >= 2) and (HashMap["o"] >= 2) and (HashMap["n"] >= 1)):
                print(HashMap)
                res += 1
                HashMap["b"] -= 1
                HashMap["a"] -= 1
                HashMap["l"] -= 2
                HashMap["o"] -= 2
                HashMap["n"] -= 1
                print(HashMap)
        return res

        

        