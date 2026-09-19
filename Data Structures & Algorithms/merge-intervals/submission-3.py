class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        ans.append(intervals[0])

        for i in range(1, len(intervals)):
            curr = intervals[i]
            last = ans[-1]

            if(last[1] >= curr[0]):
                ans[-1] = [min(curr[0], last[0]), max(curr[1], last[1])]
            else:
                ans.append(curr)
        return ans


