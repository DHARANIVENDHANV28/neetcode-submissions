class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for ele in strs:
            string = string + str(len(ele))+str('#')+ele

        return string



    def decode(self, s: str) -> List[str]:
        Output = []
        i = 0

        while i<len(s):
            j=i
            while s[j] != '#':
                j = j+1
            length = int(s[i:j])

            i = j+1
            j = i+length
            Output.append(s[i:j])
            i = j
        return Output
