class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        i = 0
        j = 0
        set_ = set()
        while j<len(s):
            if s[j] not in set_:
                set_.add(s[j])
                j+=1
                max_length = max(max_length,j-i)
            else:
                set_.remove(s[i])
                i+=1
        return max_length


        