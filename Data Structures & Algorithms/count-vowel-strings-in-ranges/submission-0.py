class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        vowels = {'a','e','i','o','u'}
        HashMap = {-1:0}
        cnt = 0
        for idx,chars in enumerate(words):
            if chars[0] in vowels and chars[-1] in vowels:
                cnt+=1
            HashMap[idx] = cnt
        
        for start,end in queries:
            ans.append(HashMap[end]-HashMap[start-1])
        return ans