class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out_list = []
        i = 0
        j = 0

        while j < len(s):
            if s[j] not in s[i:j]:
                j += 1
            else:
                out_list.append(s[i:j])
                i += 1   # slide window forward instead of jumping
        out_list.append(s[i:j])  # add final substring

        return max(len(o) for o in out_list) if s else 0
