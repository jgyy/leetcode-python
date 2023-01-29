from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if k == n:
            return [[i for i in range(1, n + 1)]]
        return self.combine(n - 1, k) + [[n] + i for i in self.combine(n - 1, k - 1)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
    print(solution.combine(1, 1))
