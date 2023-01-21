from typing import List

class Solution:
    matrix: List[List[int]]
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        self.matrix = matrix


if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s1 = Solution()
    s1.rotate(matrix1)
    print(s1.matrix)
    s1.rotate(matrix2)
    print(s1.matrix)
        