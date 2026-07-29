class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        BALLOON = {"b":1,"a":1,"l":2,"o":2,"n":1}
        res = float("+inf")
        TEXT = {"b":0,"a":0,"l":0,"o":0,"n":0}
        for c in text:
            if c in TEXT:
                TEXT[c] += 1
        for c in BALLOON:
            res = min(res, TEXT[c]//BALLOON[c])    
        return res

        

        