class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = defaultdict(list)
        indegree = defaultdict(int)

        for course in range(numCourses):
            adjList[course] = []
            indegree[course] = 0

        
        for course, dep in prerequisites:
            adjList[dep].append(course)
            indegree[course] = indegree[course] + 1

        
        queue = deque()

        for course, degree in indegree.items():
            if(degree == 0):
                queue.append(course)

        courseCompleted = 0
        order = []
        while(queue):
            pop = queue.popleft()
            courseCompleted = courseCompleted + 1
            order.append(pop)
            for course in adjList[pop]:
                indegree[course] = indegree[course] - 1
                if(indegree[course] == 0):
                    queue.append(course)

        if(courseCompleted == numCourses):
            return order
        return []


            

        

