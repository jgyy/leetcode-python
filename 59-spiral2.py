from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            matrix[i][j] = k + 1
            if matrix[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return matrix

if __name__ == "__main__":
    s = Solution()
    print(s.generateMatrix(3))
