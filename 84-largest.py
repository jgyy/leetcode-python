from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        max_area = 0
        for i in range(len(heights)):
            if not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] > heights[i]:
                    top = stack.pop()
                    if stack:
                        max_area = max(max_area, heights[top] * (i - stack[-1] - 1))
                    else:
                        max_area = max(max_area, heights[top] * i)
                stack.append(i)
        while stack:
            top = stack.pop()
            if stack:
                max_area = max(max_area, heights[top] * (len(heights) - stack[-1] - 1))
            else:
                max_area = max(max_area, heights[top] * len(heights))
        return max_area


if __name__ == "__main__":
    s = Solution()
    ones = [1] * 100000
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(s.largestRectangleArea([2, 4]))
    print(s.largestRectangleArea([1, 1]))
    print(s.largestRectangleArea(ones))
