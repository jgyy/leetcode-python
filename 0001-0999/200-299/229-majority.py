from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2, count1, count2 = None, None, 0, 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1, count1 = num, 1
            elif count2 == 0:
                num2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (num1, num2)
                if nums.count(n) > len(nums) // 3]


if __name__ == '__main__':
    print(Solution().majorityElement([3, 2, 3]))
    print(Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
    assert Solution().majorityElement([3, 2, 3]) == [3]
    assert Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2]) == [1, 2]
