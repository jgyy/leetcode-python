from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([2, 5, 6, 0, 0, 1, 2], 0))
    print(solution.search([2, 5, 6, 0, 0, 1, 2], 3))
    print(solution.search([1, 3, 1, 1, 1], 3))
    print(solution.search([1, 1, 1, 3, 1], 3))
    print(solution.search([1, 1, 1, 1, 1], 3))
    print(solution.search([1, 1, 1, 1, 1], 1))
    print(solution.search([1, 1, 1, 1, 1], 0))
    print(solution.search([1, 1, 1, 1, 1], 2))
    print(solution.search([1, 1, 1, 1, 1], 4))
    print(solution.search([1, 1, 1, 1, 1], 5))
    print(solution.search([1, 1, 1, 1, 1], 6))
    print(solution.search([1, 1, 1, 1, 1], 7))
    print(solution.search([1, 1, 1, 1, 1], 8))
    print(solution.search([1, 1, 1, 1, 1], 9))
    print(solution.search([1, 1, 1, 1, 1], 10))
    print(solution.search([1, 1, 1, 1, 1], 11))
    print(solution.search([1, 1, 1, 1, 1], 12))
    print(solution.search([1, 1, 1, 1, 1], 13))
    print(solution.search([1, 1, 1, 1, 1], 14))
    print(solution.search([1, 1, 1, 1, 1], 15))
    print(solution.search([1, 1, 1, 1, 1], 16))
