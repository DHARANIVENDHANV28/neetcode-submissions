class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ch in operations:
            if ch == "+":
                stack.append(int(stack[-1])+int(stack[-2]))
            elif ch == "D":
                stack.append(int(stack[-1])*2)
            elif ch == "C":
                stack.pop()
            else:
                stack.append(int(ch))
        return sum(stack) 


        