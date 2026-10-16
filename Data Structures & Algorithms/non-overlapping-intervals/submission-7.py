class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # [[1,2] [1,4] [2,4]]

        result = [intervals[0]]
        count = 0
        for start, end in intervals[1:]:
            if(result[-1][1] > start):
                count = count + 1
                if end < result[-1][1]:
                    result[-1] = [start, end]
                continue
            result.append([start, end])
        
        return count
            
            