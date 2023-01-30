from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            in_degree[cur] += 1
            adj[pre].append(cur)
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adj[pre]:
                in_degree[cur] -= 1
                if in_degree[cur] == 0:
                    queue.append(cur)
        return numCourses == 0


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    print(Solution().canFinish(numCourses, prerequisites))
