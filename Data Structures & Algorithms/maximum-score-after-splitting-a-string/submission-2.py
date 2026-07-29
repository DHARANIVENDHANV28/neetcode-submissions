class Solution:
    def maxScore(self, s: str) -> int:
        left = 0 if s[0] == "1" else 1
        right = -1 if s[0] == "1" else 0
        for n in s:
            right += int(n)        
        output = right+left
        for idx in range(1,len(s)-1):
            ch = s[idx]
            if ch == "0":
                left += 1
            elif ch == "1":
                right -= 1
            output = max(output,left+right)
        return output

        