class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - max(0, min(ax2, bx2) - max(ax1, bx1)) * max(0, min(ay2, by2) - max(ay1, by1))

if __name__ == '__main__':
    s = Solution()
    print(s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
    print(s.computeArea(-2, -2, 2, 2, -2, -2, 2, 2))
    print(s.computeArea(-2, -2, 2, 2, 3, 3, 4, 4))
