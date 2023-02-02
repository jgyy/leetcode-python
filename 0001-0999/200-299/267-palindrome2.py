from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def dfs(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(len(s)):
                if i > 0 and s[i] == s[i - 1]:
                    continue
                dfs(s[:i] + s[i + 1:], path + s[i], res)

        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        odd = 0
        mid = ""
        for c, v in counter.items():
            if v % 2 == 1:
                odd += 1
                mid = c
            if odd > 1:
                return []
            counter[c] = v // 2
        res = []
        dfs("".join(c * v for c, v in counter.items()), "", res)
        return [r + mid + r[::-1] for r in res]


if __name__ == '__main__':
    s = Solution()
    print(s.generatePalindromes("abc"))
    print(s.generatePalindromes("aabb"))
