class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals=sorted(intervals,key = lambda i:i[0])
        for i in intervals:
            print(stack)
            if not stack:
                stack.append(i)
            else:
                s1,e1 = stack[-1]
                s2,e2 = i[0],i[1]
                if (s1<=s2<=e1) or (s1<e2<=e1):
                    stack.pop()
                    merge = [min(s1,s2),max(e1,e2)]
                    stack.append(merge)
                else:
                    stack.append(i)
        return stack


        