from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        return 0


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    print(Solution().hIndex(citations))
