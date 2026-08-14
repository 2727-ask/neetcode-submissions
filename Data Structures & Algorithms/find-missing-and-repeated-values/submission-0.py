class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = []
        ans = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res.append(grid[i][j])

        d = Counter(res)

        n = len(res)

        for x in range(1, n + 1):
            if x not in res:
                ans.append(x)
                break

        for x, y in d.items():
            if y > 1:
                ans.append(x)
                break

        return [ans[1], ans[0]]