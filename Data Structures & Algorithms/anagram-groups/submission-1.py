class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        Output = []
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s not in hashmap:
                hashmap[sorted_s] = [s]
            else:
                hashmap[sorted_s] += [s]
        for v in hashmap.values():
            Output.append(v)
        return Output
        