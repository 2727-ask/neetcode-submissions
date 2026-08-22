class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
            ad = defaultdict(list)
            for p, c in edges:
                ad[p].append(c)
                ad[c].append(p)
            visit = set()
            flag = True

            def dfs(i,prev):
                nonlocal flag

                if i in visit:
                    flag = False
                    return False
                
                visit.add(i)
                for n in ad[i]:
                    if prev == n:
                        continue
                    dfs(n,i)
            dfs(0,-1)
            if len(visit) == n:
                return flag
            return False




        