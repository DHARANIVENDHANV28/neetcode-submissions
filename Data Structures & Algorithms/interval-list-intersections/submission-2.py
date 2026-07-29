class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j =0,0
        output = []
        while i<len(firstList) and j<len(secondList):
            startA,endA = firstList[i]
            startB,endB = secondList[j]

            start = max(startA,startB)
            end = min(endA,endB)

            if start <= end:
                output.append([start,end])

            if endA < endB:
                i += 1
            else:
                j += 1

        return output
            
                