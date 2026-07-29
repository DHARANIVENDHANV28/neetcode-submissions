class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:    
        sorted_trips = sorted(trips, key=lambda x: x[1])
        for cnt,t in enumerate(sorted_trips):
            numP,Start1,End1 = t[0],t[1],t[2]
            NumOfPass = numP
            cnt-=1
            while cnt >= 0:
                Start2,End2 = sorted_trips[cnt][1],sorted_trips[cnt][2]
                if max(Start1,Start2) < min(End1,End2):
                    NumOfPass += sorted_trips[cnt][0]
                cnt -= 1
            print(NumOfPass)
            if NumOfPass > capacity:
                return False
        return True




        