from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        low = float('-inf')
        for p in preorder:
            if p < low:
                return False
            while stack and p > stack[-1]:
                low = stack.pop()
            stack.append(p)
        return True


if __name__ == '__main__':
    preorder = [5, 2, 1, 3, 6]
    print(Solution().verifyPreorder(preorder))
