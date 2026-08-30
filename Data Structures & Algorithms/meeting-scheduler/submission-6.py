class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        i = 0
        j = 0

        slots1.sort()
        slots2.sort()

        while i<len(slots1) and j<len(slots2):
            
            s1,e1 = slots1[i]
            s2,e2 =  slots2[j]

            #overlap
            maxS = max(s1,s2)
            minE = min(e1,e2)
            if maxS < minE:
                if minE-maxS >= duration:
                    return [maxS,maxS+duration]
            #moving pointers
            if e1<e2:
                i+=1
            elif e1>e2:
                j+=1
            else:
                i+=1
                j+=1
        return []










































        output = []
        slots1.sort()
        slots2.sort()

        i = 0
        j = 0

        while i<len(slots1) and j<len(slots2):
            s = max(slots1[i][0],slots2[j][0])
            e = min(slots1[i][1],slots2[j][1])

            if e - s >= duration:
                return [s,s+duration]

            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1

            

        return output


        