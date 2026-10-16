"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)

        end_times = []
        max_rooms = 0

        for interval in intervals:
            while end_times and end_times[0] <= interval.start:
                heapq.heappop(end_times)

            heapq.heappush(end_times, interval.end)
            max_rooms = max(max_rooms, len(end_times))
        
        return max_rooms
        