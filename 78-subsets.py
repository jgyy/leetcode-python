from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [item + [num] for item in result]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
