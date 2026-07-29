# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         string = s[0]
#         def dfs(i,j):
#             if j>len(s):
#                 return
#             if self.palindrome(s[i:j]):
#                 if len(string) < len(s[i:j]):
#                     string = s[i:j]
            
#             dfs(i,j+1)
#             i = j-1
#             dfs(i,j+1)
#         dfs(0,1)
#         return string

#     def palindrome(self,string):
#             if string == string[::-1]:
#                 return True
#             else:
#                 return False
            
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        # Use nonlocal for string to modify it inside dfs
        longest = s[0]  # Initialize with the first character

        def dfs(i, j):
            nonlocal longest
            if j > len(s):
                return
            # Check if the substring s[i:j] is a palindrome
            if self.palindrome(s[i:j]):
                # Update longest palindrome found
                if len(s[i:j]) > len(longest):
                    longest = s[i:j]
            # Explore further by increasing j
            dfs(i, j + 1)

        # Start dfs for each character
        for i in range(len(s)):
            dfs(i, i + 1)  # Start checking substrings starting from s[i]

        return longest

    def palindrome(self, string):
        return string == string[::-1]
