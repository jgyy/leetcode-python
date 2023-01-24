from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]
        for n in nums:
            subsets += [s + [n] for s in subsets if s + [n] not in subsets]
        return subsets


if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))
