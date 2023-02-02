from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] == len(citations) - mid:
                return citations[mid]
            elif citations[mid] < len(citations) - mid:
                left = mid + 1
            else:
                right = mid - 1
        return len(citations) - left


if __name__ == '__main__':
    print(Solution().hIndex([0, 1, 3, 5, 6]))
    assert Solution().hIndex([0, 1, 3, 5, 6]) == 3
    print(Solution().hIndex([1, 2, 100]))
    assert Solution().hIndex([1, 2, 100]) == 2
