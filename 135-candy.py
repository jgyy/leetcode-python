from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                right[i - 1] = right[i] + 1
        return sum(max(left[i], right[i]) for i in range(n))


if __name__ == '__main__':
    print(Solution().candy([1, 0, 2]))
    print(Solution().candy([1, 2, 2]))
    assert Solution().candy([1, 0, 2]) == 5
    assert Solution().candy([1, 2, 2]) == 4
