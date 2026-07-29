class Solution:
    def climbStairs(self, n: int) -> int:
        output = []
        def BT(sub,Sum):
            if Sum >= n:
                if Sum == n:
                    output.append(sub.copy())
                return 
            sub.append(1)
            BT(sub,Sum+1)
            sub.pop()
            BT(sub,Sum+2)
        BT([],0)
        return len(output)


        