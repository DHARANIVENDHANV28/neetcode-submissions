class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for w in words:
            flag = True
            for s in w:
                if s not in allowed:
                    flag = False
                    break
            if flag:
                res += 1
        return res


        