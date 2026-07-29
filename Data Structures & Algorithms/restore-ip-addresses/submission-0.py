class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = []
        def dfs(idx,parts,string):
            if parts == 4:
                if idx == len(s):
                    output.append(string[:-1])
                return
            for i in range(1,4):
                if idx+i>len(s):
                    break
                num = s[idx:idx+i]
                if int(num)>255 or (num[0] == "0" and len(num)>1):
                    continue

                dfs(idx+i,parts+1,string+num+str('.')) 
        dfs(0,0,"")
        return output

        