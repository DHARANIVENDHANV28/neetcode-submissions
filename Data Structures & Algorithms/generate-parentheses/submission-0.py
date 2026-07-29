class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack,res = [],[]

        def BT(num_open,num_close):
            #basecase
            if num_open == num_close == n:
                res.append(''.join(stack))
                return
            else:
                if num_open<n:
                    stack.append('(')
                    BT(num_open+1,num_close)
                    stack.pop()     
                if num_close<num_open:
                    stack.append(')')
                    BT(num_open,num_close+1)
                    stack.pop()
        BT(0,0)
        return res   