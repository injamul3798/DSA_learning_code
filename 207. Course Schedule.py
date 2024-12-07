from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        indegree = {}
        
        for i in range(numCourses):
            graph[i] = []

        for i in range(numCourses):
            indegree[i] = 0

        # Now create a graph and fidngin indegree
        for v,u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1


        queue = deque()
        for u in indegree:
            if indegree[u] == 0:
                queue.append(u)


        courseTaken = 0
        while queue:
            current = queue.popleft()
            courseTaken += 1

            for v in graph[current]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return courseTaken == numCourses
 
        
