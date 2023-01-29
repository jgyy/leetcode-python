class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


if __name__ == '__main__':
    n = 43261596
    print(Solution().reverseBits(n))
