from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col-1]
        self.matrix = matrix

    def update(self, row: int, col: int, val: int) -> None:
        if col == 0:
            diff = val - self.matrix[row][col]
        else:
            diff = val - (self.matrix[row][col] - self.matrix[row][col-1])
        for i in range(col, len(self.matrix[0])):
            self.matrix[row][i] += diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2+1):
            if col1 == 0:
                total += self.matrix[row][col2]
            else:
                total += self.matrix[row][col2] - self.matrix[row][col1-1]
        return total


if __name__ == "__main__":
    obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [
                    1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(obj.sumRegion(2, 1, 4, 3))
    obj.update(3, 2, 2)
    print(obj.sumRegion(2, 1, 4, 3))
