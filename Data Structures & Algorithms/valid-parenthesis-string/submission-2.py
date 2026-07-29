class Solution:
    def checkValidString(self, s: str) -> bool:
        maxLeft, minLeft = 0,0
        for c in s:
            if c == '(':
                maxLeft += 1
                minLeft += 1
            elif c == ')':
                maxLeft -= 1
                minLeft -= 1
            else:
                maxLeft += 1
                minLeft -= 1
            if maxLeft < 0:
                return False
            if minLeft < 0:
                minLeft = 0
        return minLeft == 0