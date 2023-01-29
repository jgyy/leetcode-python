from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        nums = [lower - 1] + nums + [upper + 1]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 2:
                res.append(str(nums[i] - 1))
            elif nums[i] - nums[i - 1] > 2:
                res.append(str(nums[i - 1] + 1) + "->" + str(nums[i] - 1))
        return res


if __name__ == '__main__':
    print(Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99))
    assert Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99) == [
        "2", "4->49", "51->74", "76->99"]
