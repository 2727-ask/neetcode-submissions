class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last = intervals[0][-1]

        count = 0
        for start, end in intervals[1:]:
            if(last > start):
                count = count + 1
                last = min(last, end)
            else:
                last = end
        return count
            
        