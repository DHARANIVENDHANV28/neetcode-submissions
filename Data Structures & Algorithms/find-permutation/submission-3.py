class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = [1]

        n = 2

        for idx,c in enumerate(s):
            cur = idx
            tmp = []
            if c == "I":
                stack.append(n)
            else:
                while stack and s[cur] == "D":
                    num = stack.pop()
                    tmp.append(num)
                    cur -= 1
                stack.append(n)
                stack.extend(tmp[::-1])
            # print(stack)
            n+=1
        return stack