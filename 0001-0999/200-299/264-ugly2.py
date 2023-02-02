class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
        return ugly[-1]


if __name__ == '__main__':
    n1 = 10
    print(Solution().nthUglyNumber(n1))
    n2 = 11
    print(Solution().nthUglyNumber(n2))
    n3 = 12
    print(Solution().nthUglyNumber(n3))
