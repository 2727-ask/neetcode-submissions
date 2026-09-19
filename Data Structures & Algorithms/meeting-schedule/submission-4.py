"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)
        print(intervals)

        [(0,3), (3,6), (5,10)]
        
        last = intervals[0].end

        for interval in intervals[1:]:
            if(interval.start < last):
                return False
            else:
                last = max(last, interval.end)
        return True
