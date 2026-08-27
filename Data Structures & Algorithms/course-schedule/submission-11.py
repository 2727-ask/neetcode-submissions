class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        deps = defaultdict(int)
        adjList = defaultdict(list)
        for n in range(numCourses):
            deps[n]
    
        for x, y in prerequisites:
            if(x == y):
                return False
            deps[x] = deps[x] + 1
            adjList[y].append(x)

        queue = deque([])

        for x, y in deps.items():
            if(y == 0):
                queue.append(x)
        
        finish = 0
        while(queue):
            pop = queue.popleft()
            finish = finish + 1
            for x in adjList[pop]:   
                deps[x] = deps[x] - 1    
                if(deps[x] == 0):
                    queue.append(x)
        
        print(finish)

        return finish == numCourses
            


            
            
        




        

        