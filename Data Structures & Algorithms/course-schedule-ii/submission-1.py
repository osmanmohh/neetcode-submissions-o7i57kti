from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()
        res = []

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        for node, deg in enumerate(indegree):
            if deg == 0:
                q.append(node)
        print(dict(graph))
        print(indegree)
        while q:
            node = q.popleft()
            res.append(node)
            for course in graph[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        
        return res if len(res) == numCourses else []

        