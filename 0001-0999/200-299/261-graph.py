from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = set()
        stack = [0]
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return len(visited) == n


if __name__ == '__main__':
    n1 = 5
    edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(Solution().validTree(n1, edges1))
    n2 = 4
    edges2 = [[2, 3], [1, 2], [1, 3]]
    print(Solution().validTree(n2, edges2))
