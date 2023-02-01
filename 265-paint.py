from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
                costs[i][j] += min(costs[i - 1][:j] + costs[i - 1][j + 1:])
        return min(costs[-1])


if __name__ == '__main__':
    costs = [[1, 5, 3], [2, 9, 4]]
    print(Solution().minCostII(costs))
