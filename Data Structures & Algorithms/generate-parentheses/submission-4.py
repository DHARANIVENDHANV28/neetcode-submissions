class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(OPEN,CLOSE,sub):
            #BC
            if OPEN==CLOSE==n:
                res.append("".join(sub.copy()))
                return None
            
            #open
            if OPEN<n:
                sub.append('(')
                dfs(OPEN+1,CLOSE,sub)
                sub.pop()

            #close
            if CLOSE<OPEN:
                sub.append(')')
                dfs(OPEN,CLOSE+1,sub)
                sub.pop()

            return None

        dfs(1,0,['('])
        return res      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # output = []
        # def dfs(sub,op,cl):
        #     #Basecase
        #     if op == n and cl == n:
        #         output.append("".join(sub.copy()))
        #         return 
            
        #     # print(''.join(sub),op,cl)
        #     if op < n:
        #         sub.append('(')
        #         dfs(sub,op+1,cl)
        #         sub.pop()
            
        #     # print(''.join(sub),op,cl)
        #     if cl<op:
        #         sub.append(')')
        #         dfs(sub,op,cl+1)
        #         sub.pop()

        # dfs([],0,0)
        # return output

        