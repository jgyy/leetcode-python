from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for cur, pre in prerequisites:
            graph[pre].append(cur)
            indegrees[cur] += 1
        res = []
        queue = [i for i in range(numCourses) if indegrees[i] == 0]
        while queue:
            pre = queue.pop(0)
            res.append(pre)
            for cur in graph[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)
        return res if len(res) == numCourses else []


if __name__ == '__main__':
    print(Solution().findOrder(2, [[1, 0]]))
