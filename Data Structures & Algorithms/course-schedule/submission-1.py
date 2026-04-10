from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for pre, course in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        for node, deg in enumerate(indegree):
            if deg == 0:
                q.append(node)
        
        res  = 0
        while q:
            node = q.popleft()
            res += 1
            for course in graph[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        return res == numCourses