from typing import List


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                self.count -= 1

        self.count = 0
        parent = [-1] * (m * n)
        res = []
        for x, y in positions:
            i = x * n + y
            if parent[i] == -1:
                parent[i] = i
                self.count += 1
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    x2, y2 = x + dx, y + dy
                    j = x2 * n + y2
                    if 0 <= x2 < m and 0 <= y2 < n and parent[j] != -1:
                        union(i, j)
            res.append(self.count)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))
    print(s.numIslands2(8, 2, [[6, 0], [4, 0], [2, 1], [
          3, 1], [6, 1], [7, 1], [5, 1], [0, 0], [1, 0]]))
    print(s.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))
    print(s.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))
