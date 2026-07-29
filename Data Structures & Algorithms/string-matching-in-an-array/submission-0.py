class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []
        for idx1 in range(len(words)):
            for idx2 in range(len(words)):
                if idx1 != idx2 and words[idx1] in words[idx2]:
                    output.append(words[idx1])
                    break
        return output

