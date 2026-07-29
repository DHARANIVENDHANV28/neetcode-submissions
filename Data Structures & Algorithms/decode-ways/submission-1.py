class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)

        # hashset = set(str(i) for i in range(1,27))
        # output = []
        # def dfs(sub,idx):
        #     if idx>=len(s):
        #         output.append(sub.copy())
        #         return

        #     for j in range(idx,len(s)):
        #         if s[idx:j+1] in hashset :
        #             sub.append(s[idx:j+1])
        #             dfs(sub,j+1)
        #             sub.pop()

        # dfs([],0)
        # return len(output)
        