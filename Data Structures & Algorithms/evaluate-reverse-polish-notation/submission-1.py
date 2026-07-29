class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i != '/' :
                stack.append(int(i))
            if i == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a+b)
            if i == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)

            if i == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a*b)
            if i == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(float(b)/a))
        return stack[0]

        