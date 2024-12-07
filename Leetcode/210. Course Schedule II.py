from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        indegree = {}

        for i in range(numCourses):
            graph[i] = []

        for i in range(numCourses):
            indegree[i] = 0

        # Now making the graph and setting indegree of every element
        for v,u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque()
        for u in indegree:
            if indegree[u] == 0:
                queue.append(u)
        courses = []
        while(queue):
            current = queue.popleft()
            courses.append(current)

            for v in graph[current]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        if len(courses) == numCourses:
            return courses
        else:
            return []
        
