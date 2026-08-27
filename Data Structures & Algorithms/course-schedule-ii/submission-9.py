class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = defaultdict(int)
        adjList = defaultdict(list)

        for course in range(numCourses):
            indegree[course] = 0

        for course, preq in prerequisites:
            indegree[course] = indegree[course] + 1 
            adjList[preq].append(course)

        queue = deque()
        for course in range(numCourses):
            if(indegree[course] == 0):
                queue.append(course)
        res = []
        while queue:
            pop = queue.popleft()
            res.append(pop)
            for course in adjList[pop]:
                indegree[course] = indegree[course] - 1 
                if(indegree[course] == 0):
                    queue.append(course)
        if(len(res) != numCourses):
            return []
        return res

        