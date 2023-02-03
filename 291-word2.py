class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def dfs(i, j):
            if i == len(pattern) and j == len(s):
                return True
            if i >= len(pattern) or j >= len(s):
                return False
            if pattern[i] in dic:
                if not s.startswith(dic[pattern[i]], j):
                    return False
                return dfs(i+1, j+len(dic[pattern[i]]))
            for k in range(j, len(s)):
                if s[j:k+1] in dic.values():
                    continue
                dic[pattern[i]] = s[j:k+1]
                if dfs(i+1, k+1):
                    return True
                del dic[pattern[i]]
            return False
        dic = {}
        return dfs(0, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.wordPatternMatch("abab", "redblueredblue"))
    print(s.wordPatternMatch("aaaa", "asdasdasdasd"))
    print(s.wordPatternMatch("aabb", "xyzabcxzyabc"))
