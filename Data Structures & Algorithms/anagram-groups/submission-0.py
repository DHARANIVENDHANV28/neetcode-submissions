class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HashMap = {}
        Output = []
        for word in strs:
            result = "".join(sorted(word))
            if result in HashMap:
                HashMap[result] += [word]
            else:
                HashMap[result] = [word]
        print(HashMap)

        for key,values in HashMap.items():
            Output.append(values)

        return Output
        


        