from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit for digit, group in groupby(s))
        return s


if __name__ == "__main__":
    print(Solution().countAndSay(1))
    print(Solution().countAndSay(4))
    print(Solution().countAndSay(5))
