from typing import List


class Solution:
    matrix: List[List[int]]

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        self.matrix = matrix


if __name__ == '__main__':
    solution = Solution()
    solution.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    print(solution.matrix)
    solution.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
    print(solution.matrix)
