from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            row = [0] * i
            row[0] = 1
            row[-1] = 1
            for j in range(1, i - 1):
                row[j] = result[i - 2][j - 1] + result[i - 2][j]
            result.append(row)
        return result


if __name__ == "__main__":
    print(Solution().generate(5))
    print(Solution().generate(1))
    print(Solution().generate(0))
