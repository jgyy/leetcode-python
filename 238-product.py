from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L, R, answer = [0]*n, [0]*n, [0]*n
        L[0] = 1
        for i in range(1, n):
            L[i] = nums[i-1] * L[i-1]
        R[n-1] = 1
        for i in reversed(range(n-1)):
            R[i] = nums[i+1] * R[i+1]
        for i in range(n):
            answer[i] = L[i] * R[i]
        return answer


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))
