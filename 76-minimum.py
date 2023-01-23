from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = start = end = 0
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            if not missing:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if not end or right - left <= end - start:
                    start, end = left, right
        return s[start:end]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))
    print(solution.minWindow("a", "a"))
    print(solution.minWindow("a", "aa"))
