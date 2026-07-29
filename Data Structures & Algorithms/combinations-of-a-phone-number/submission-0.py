class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        output = []
        def dfs(idx,sub):
            if idx >= len(digits):
                output.append("".join(sub.copy()).strip())
                return 
            for i in range(0,len(hashmap[digits[idx]])):
                sub.append(hashmap[digits[idx]][i])
                dfs(idx+1,sub)
                sub.pop()
        dfs(0,[])    
        return output if digits != "" else []
        