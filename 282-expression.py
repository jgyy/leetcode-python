from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(num: str, target: int, path: str, value: int, pre: int) -> None:
            if not num and value == target:
                result.append(path)
                return
            for i in range(1, len(num) + 1):
                if i > 1 and num[0] == '0':
                    continue
                cur = int(num[:i])
                if not path:
                    dfs(num[i:], target, num[:i], cur, cur)
                else:
                    dfs(num[i:], target, path + '+' +
                        num[:i], value + cur, cur)
                    dfs(num[i:], target, path + '-' +
                        num[:i], value - cur, -cur)
                    dfs(num[i:], target, path + '*' + num[:i],
                        value - pre + pre * cur, pre * cur)
        result = []
        dfs(num, target, '', 0, 0)
        return result


if __name__ == '__main__':
    print(Solution().addOperators('123', 6))
    print(Solution().addOperators('232', 8))
    print(Solution().addOperators('105', 5))
    print(Solution().addOperators('00', 0))
    print(Solution().addOperators('3456237490', 9191))
