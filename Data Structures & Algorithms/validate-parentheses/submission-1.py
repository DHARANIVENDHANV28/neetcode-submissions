class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {')':'(',
                    '}':'{',
                    ']':'['}
        for bracket in s:
            if bracket not in hash_map:
                stack.append(bracket)
                continue
            if not stack or hash_map[bracket] != stack[-1]:
                return False
            if hash_map[bracket] == stack[-1]:
                stack.pop()
        return not stack 
        