class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = []
        for q in queries:
            minLen = float("+inf")
            Found = False
            for i in intervals:
                s,e = i[0],i[1]
                if s<=q<=e:
                    Found = True
                    length = e-s+1
                    minLen = min(minLen,length)
            if Found:
                output.append(minLen)
            else:
                output.append(-1)

        return output
        