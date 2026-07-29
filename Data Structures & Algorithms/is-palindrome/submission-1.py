class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [i for i in s if i.isalnum()]
        string = "".join(string)
        string = string.lower()
        print(string)
        left = 0
        right = len(string)-1
        while left<right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


        