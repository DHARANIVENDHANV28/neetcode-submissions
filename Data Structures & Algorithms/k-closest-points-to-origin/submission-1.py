class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def DistanceFromOrigin(x,y):
            return round((x**2+y**2)**(0.5),2)
        res = []
        for p in points:
            res.append((DistanceFromOrigin(p[0],p[1]),[p[0],p[1]]))
        print(sorted(res))
        return [j[1] for i,j in enumerate(sorted(res)) if i<k]


        