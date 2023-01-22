class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 1. initialize the factorial array
        factorial = [1]
        for i in range(1, n + 1):
            factorial.append(factorial[-1] * i)

        # 2. initialize the number array
        nums = [i for i in range(1, n + 1)]

        # 3. get the kth permutation
        k -= 1
        ans = []
        for i in range(1, n + 1):
            idx = k // factorial[n - i]
            ans.append(str(nums[idx]))
            nums.pop(idx)
            k -= idx * factorial[n - i]

        return ''.join(ans)


if __name__ == '__main__':
    n = 3
    k = 3
    print(Solution().getPermutation(n, k)) # 213
