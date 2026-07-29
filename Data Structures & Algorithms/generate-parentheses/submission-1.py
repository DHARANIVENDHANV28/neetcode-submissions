class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def dfs(sub,op,cl):
            #Basecase
            if op == n and cl == n:
                output.append("".join(sub.copy()))
                return 
            
            # print(''.join(sub),op,cl)
            if op < n:
                sub.append('(')
                dfs(sub,op+1,cl)
                sub.pop()
            
            # print(''.join(sub),op,cl)
            if cl<op:
                sub.append(')')
                dfs(sub,op,cl+1)
                sub.pop()

        dfs([],0,0)
        return output

        