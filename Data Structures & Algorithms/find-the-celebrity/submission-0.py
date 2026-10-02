# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        indeg = [0]*n
        outdeg = [0]*n
        for n1 in range(n):
            for n2 in range(n):
                if n1==n2:
                    continue
                if knows(n1,n2):
                    indeg[n2]+=1
                    outdeg[n1]+=1
                
                print(n1,n2,knows(n1,n2))
        print(indeg,outdeg)
        for idx in range(n):
            if indeg[idx] == n-1 and outdeg[idx]==0:
                return idx
        return -1
        
        