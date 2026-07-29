class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] #(s,idx)
        delete = set()
        for idx,ch in enumerate(s):
            if ch == "(":
                stack.append(idx)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    delete.add(idx)
        while stack:
            delete.add(stack.pop())

        result = []

        for idx,ch in enumerate(s):
            if idx not in delete:
                result.append(ch)
        return "".join(result)
        


        