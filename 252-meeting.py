from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(Solution().canAttendMeetings(intervals))
