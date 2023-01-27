from typing import List
# The read4 API is already defined for you.


def read4(buf4: List[str]) -> int:
    return len(buf4)


class Solution:
    def __init__(self):
        self.q = []

    def read(self, buf, n):
        i = 0
        while i < n:
            if self.q:
                buf[i] = self.q.pop(0)
                i += 1
            else:
                buf4 = ['']*4
                v = read4(buf4)
                if v == 0:
                    break
                self.q += buf4[:v]
        return i


if __name__ == '__main__':
    print(Solution().read([*"abc"], 4))
    print(Solution().read([*"abcde"], 5))
    print(Solution().read([*"abcdABCD1234"], 12))
