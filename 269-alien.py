from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Build graph
        graph = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
            else:
                if len(words[i]) > len(words[i + 1]):
                    return ""

        # Topological sort
        visited = {}
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = False
            for n in graph[c]:
                if not dfs(n):
                    return False
            visited[c] = True
            res.append(c)
            return True

        for c in graph:
            if not dfs(c):
                return ""
        return "".join(res[::-1])


if __name__ == '__main__':
    print(Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
    print(Solution().alienOrder(["abc", "ab"]))
    print(Solution().alienOrder(["aba"]))
