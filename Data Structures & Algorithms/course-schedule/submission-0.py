from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        res = []
        q = deque()
        for node, degree in enumerate(indegree):
            if degree == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            res.append(node)
            for course in graph[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        return len(res) == numCourses
