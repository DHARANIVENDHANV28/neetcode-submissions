class Solution:
    def expand(self, s: str) -> List[str]:
        sf = []
        i = 0
        while i<len(s):
            if s[i] == '{':
                i = i+1
                string = ''
                while s[i] != '}':
                    if s[i].isalpha():
                        string += s[i]
                    i += 1
                sf.append(string)
            else:
                sf.append(s[i])
            i += 1
        print(sf)

        def dfs(idx,sub):
            if idx>=len(sf):
                res.append("".join(sub.copy()))
                return None
            
            for c in sf[idx]:
                sub.append(c)
                dfs(idx+1,sub)
                sub.pop()
            return None
        res = []
        dfs(0,[])
        return res

            
