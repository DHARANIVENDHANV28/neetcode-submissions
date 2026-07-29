class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def DistanceFromOrigin(p):
            return (round((p[0]**2+p[1]**2)**(0.5),2),p) #(dist,[x,y])
    
        dist = []
        for p in points:
            dist.append(DistanceFromOrigin(p))
        heapq.heapify(dist)
        res = []
        i = 0
        while k>i:
            distance,[x,y] = heapq.heappop(dist)
            res.append([x,y])
            i+=1
        return res

        
        
        
        # def DistanceFromOrigin(x,y):
        #     return round((x**2+y**2)**(0.5),2)
        # res = []
        # for p in points:
        #     res.append((DistanceFromOrigin(p[0],p[1]),[p[0],p[1]]))
        # print(sorted(res))
        # return [j[1] for i,j in enumerate(sorted(res)) if i<k]


        