from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        left, right = y, y
        top, bottom = x, x
        for i in range(m):
            for j in range(n):
                if image[i][j] == "1":
                    left = min(left, j)
                    right = max(right, j)
                    top = min(top, i)
                    bottom = max(bottom, i)
        return (right - left + 1) * (bottom - top + 1)


if __name__ == '__main__':
    s = Solution()
    print(s.minArea([["0", "0", "1", "0"], [
          "0", "1", "1", "0"], ["0", "1", "0", "0"]], 0, 2))
    print(s.minArea([["1"]], 0, 0))
    print(s.minArea([["0", "0", "1", "0"], [
          "0", "1", "1", "0"], ["0", "1", "0", "0"]], 0, 1))
