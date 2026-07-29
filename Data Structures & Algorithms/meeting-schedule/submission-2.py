"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i:i.start)

        for i in range(1,len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True
















        # lis = []                 #O(n)
        # for obj in intervals:    #O(n)
        #     lis.append((obj.start,obj.end))
        # sorted_lis = sorted(lis) #O(nlogn)
        # print(sorted_lis)

        # for i,inter in enumerate(sorted_lis):
        #     if i == 0:
        #         end = inter[1]
        #         continue
        #     if i > 0:
        #         start = inter[0]
        #     if start >= end:
        #         end = inter[1]
        #         continue
        #     else:
        #         return False
        # return True
            
