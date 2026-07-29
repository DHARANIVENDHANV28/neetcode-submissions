class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        max_ws = 0
        while r < len(s):
            ws = r - l + 1
            dict_ = {}
            for i in s[l:r+1]:
                if i in dict_:
                    dict_[i] += 1
                else:
                    dict_[i] = 1
            mf = max(dict_.values())

            if ws-mf <= k:
                r += 1
                max_ws = max(max_ws,ws)
            else:
                l += 1
        return max_ws

