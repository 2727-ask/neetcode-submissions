class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
            ad = defaultdict(list)
            for p, c in edges:
                ad[p].append(c)
                ad[c].append(p)
            visit = set()

            def dfs(i,prev):
                if i in visit:
                    return False
                visit.add(i)
                for nei in ad[i]:
                    if prev == nei:
                        continue
                    if not dfs(nei,i):
                        return False
                return True

            if dfs(0,-1):
                return len(visit) == n
            else:
                return False




        