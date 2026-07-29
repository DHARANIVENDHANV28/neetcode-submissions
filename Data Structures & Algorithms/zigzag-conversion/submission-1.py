class Solution:
    def convert(self, s: str, numRows: int) -> str:
        LEN,i = 0,0
        HashMap = {}
        while LEN < len(s):
            while i < numRows and LEN < len(s):
                if i not in HashMap:
                    HashMap[i] = []
                HashMap[i] += s[LEN]
                i+=1
                LEN+=1
            i-=1
            while i != 0 and LEN < len(s):
                i-=1
                if i not in HashMap:
                    HashMap[i] = []
                HashMap[i] += s[LEN]
                LEN+=1
            i+=1
        res = ""
        for i in range(numRows):
            if i not in HashMap:
                break
            res += "".join(HashMap[i])
        return res