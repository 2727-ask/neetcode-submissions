class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [x for x in range(numCourses)]

        adjList = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for parent, child in prerequisites:
            adjList[child].append(parent)
            indegree[parent] = indegree[parent] + 1 

        queue = deque([])

        for key, val in indegree.items():
            if(val == 0):
                queue.append(key)

        order = []
        while queue:
            pop = queue.popleft()
            order.append(pop)
            for child in adjList[pop]:
                indegree[child] =  indegree[child] - 1
                if(indegree[child] == 0):
                    queue.append(child)

        if(len(order) != numCourses):
            return []

        return order




