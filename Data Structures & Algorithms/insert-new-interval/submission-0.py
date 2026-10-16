class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i, interval in enumerate(intervals):
            if(interval[1] < newInterval[0]):
                result.append(interval)
            elif(interval[0] > newInterval[1]):
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]
        result.append(newInterval)
        return result