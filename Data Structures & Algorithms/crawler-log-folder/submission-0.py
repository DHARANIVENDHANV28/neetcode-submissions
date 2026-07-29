class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for l in logs:
            if stack and l == "../":
                stack.pop()
            elif l != "../" and l != "./":
                stack.append(l)
            print(stack)
        return len(stack)
        