"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        lis = []
        for obj in intervals:
            lis.append((obj.start,obj.end))
        sorted_lis = sorted(lis)
        print(sorted_lis)

        for i,inter in enumerate(sorted_lis):
            if i == 0:
                end = inter[1]
                continue
            if i > 0:
                start = inter[0]
            if start >= end:
                end = inter[1]
                continue
            else:
                return False
        return True
            
