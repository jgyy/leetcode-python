from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] + 1:
                continue
            start = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                i += 1
            end = nums[i]
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + '->' + str(end))
        return res


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    print(Solution().summaryRanges(nums))
