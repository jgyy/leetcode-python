from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1]:
                right.append(interval)
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        return left + [newInterval] + right


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(Solution().insert(intervals, newInterval))
