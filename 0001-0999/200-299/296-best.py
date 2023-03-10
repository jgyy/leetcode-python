from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        rows.sort()
        cols.sort()
        row = rows[len(rows) // 2]
        col = cols[len(cols) // 2]
        return sum(abs(row - rows[i]) + abs(col - cols[i]) for i in range(len(rows)))


if __name__ == '__main__':
    print(Solution().minTotalDistance(
        [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
    assert Solution().minTotalDistance(
        [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]) == 6
