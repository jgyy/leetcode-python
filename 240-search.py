from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True

        return False


if __name__ == '__main__':
    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print(Solution().searchMatrix(matrix1, 3))
    print(Solution().searchMatrix(matrix1, 13))
    matrix2 = [[1, 4], [2, 5]]
    print(Solution().searchMatrix(matrix2, 2))
    matrix3 = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(Solution().searchMatrix(matrix3, 5))
