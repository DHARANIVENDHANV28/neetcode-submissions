class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []

        for p in paths:
            if stack and p == "..":
                stack.pop()
            elif p == ".." or p == "." or p == "":
                continue
            else:
                stack.append(p)
        print("/"+"/".join(stack))
        return "/"+"/".join(stack)
         

