class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        output = []
        cur = []
        wordDict = set(wordDict)
        def dfs(start):

            if start == len(s):
                output.append(" ".join(cur))
                return 

            for end in range(start,len(s)):
                w = s[start:end+1]
                if w in wordDict:
                    cur.append(w)
                    dfs(end+1)
                    cur.pop()

        dfs(0)
        return output
        


        