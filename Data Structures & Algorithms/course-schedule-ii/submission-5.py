class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [x for x in range(numCourses)]

        indegree = {i:0 for i in range(numCourses)}
        adjList = defaultdict(list)

        for courses in prerequisites:
            child = courses[0]
            parent = courses[1]
            indegree[child] = indegree[child] + 1
            adjList[parent].append(child)

        queue = deque([])

        print(indegree)

        for key, val in indegree.items():
            if(val == 0):
                queue.append(key)
        
        order = []
        while queue:
            pop = queue.popleft()
            order.append(pop)

            for course in adjList[pop]:
                indegree[course] = indegree[course] - 1 

                if(indegree[course] == 0):
                    queue.append(course)
        if(len(order) != numCourses):
            return []
        return order


