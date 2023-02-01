from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms = []
        for interval in intervals:
            i = 0
            while i < len(rooms):
                if rooms[i] <= interval[0]:
                    rooms[i] = interval[1]
                    break
                i += 1
            if i == len(rooms):
                rooms.append(interval[1])
        return len(rooms)


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(Solution().minMeetingRooms(intervals))
