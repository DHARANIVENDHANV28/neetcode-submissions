class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j =0,0
        output = []
        while i<len(firstList) and j<len(secondList):
            a1,a2 = firstList[i][0],firstList[i][1]
            b1,b2 = secondList[j][0],secondList[j][1]
            intersec = ["a","a"]
            if b1<=a1<=b2:
                intersec[0] = a1
            if b1<=a2<=b2:
                intersec[1] = a2
            if a1<=b1<=a2:
                intersec[0] = b1
            if a1<=b2<=a2:
                intersec[1] = b2
            if len(intersec) == 2 and (intersec[0] != "a" or intersec[1] != "a"):
                output.append(intersec)
            if a2>b2:
                j+=1
            elif b2>a2:
                i+=1
            else:
                i+=1
                j+=1
        return output
            
                