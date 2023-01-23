from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        max_area = 0
        heights = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            stack = []
            for j in range(len(heights)):
                if not stack or heights[stack[-1]] <= heights[j]:
                    stack.append(j)
                else:
                    while stack and heights[stack[-1]] > heights[j]:
                        top = stack.pop()
                        if stack:
                            max_area = max(
                                max_area, heights[top] * (j - stack[-1] - 1))
                        else:
                            max_area = max(max_area, heights[top] * j)
                    stack.append(j)
            while stack:
                top = stack.pop()
                if stack:
                    max_area = max(
                        max_area, heights[top] * (len(heights) - stack[-1] - 1))
                else:
                    max_area = max(max_area, heights[top] * len(heights))
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maximalRectangle([["1", "0", "1", "0", "0"],
                              ["1", "0", "1", "1", "1"],
                              ["1", "1", "1", "1", "1"],
                              ["1", "0", "0", "1", "0"]]))
    print(s.maximalRectangle([["0", "1"],
                              ["1", "0"]]))
    print(s.maximalRectangle([["0"]]))
    print(s.maximalRectangle([["1"]]))
    print(s.maximalRectangle([["1", "1"]]))
    print(s.maximalRectangle([["1", "1", "1"]]))
    print(s.maximalRectangle([["1", "1", "1", "1"]]))
    print(s.maximalRectangle([["1", "1", "1", "1", "1"]]))
    print(s.maximalRectangle([["1", "1", "1", "1", "1", "1"]]))
    print(s.maximalRectangle([["1", "1", "1", "1", "1", "1", "1"]]))
    print(s.maximalRectangle([["1", "1", "1", "1", "1", "1", "1", "1"]]))
    print(s.maximalRectangle([["1", "1", "1", "1", "1", "1", "1", "1", "1"]]))
    print(s.maximalRectangle(
        [["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]))
    print(s.maximalRectangle(
        [["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]))
    print(s.maximalRectangle(
        [["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]))
    print(s.maximalRectangle(
        [["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]))
