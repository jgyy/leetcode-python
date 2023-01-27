from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        res = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cnt = 0
                for x3, y3 in points:
                    if (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1):
                        cnt += 1
                res = max(res, cnt)
        return res


if __name__ == '__main__':
    print(Solution().maxPoints([[1, 1], [2, 2], [3, 3]]))
    print(Solution().maxPoints(
        [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
    assert Solution().maxPoints([[1, 1], [2, 2], [3, 3]]) == 3
    assert Solution().maxPoints(
        [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
