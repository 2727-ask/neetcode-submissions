class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if(not prerequisites):
            return True
            
        indegree = {i: 0 for i in range(numCourses)}
        adjList = defaultdict(list)
        for courses in prerequisites:
            parent = courses[0]
            child = courses[1]

            adjList[parent].append(child)

            if(parent not in indegree):
                indegree[parent] = 0
            indegree[child] = indegree[child] + 1

        queue = deque([])

        for course, degree in indegree.items():
            if(degree == 0):
                queue.append(course)
        
        count = 0
        while queue:
            pop = queue.popleft()
            count = count + 1

            for child in adjList[pop]:
                indegree[child] = indegree[child] - 1

                if(indegree[child] == 0):
                    queue.append(child)

        return (count == numCourses)


        


        
        