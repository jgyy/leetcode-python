class Solution:
    def canWin(self, currentState: str) -> bool:
        for i in range(len(currentState) - 1):
            if currentState[i:i+2] == "++":
                nextState = currentState[:i] + "--" + currentState[i+2:]
                if not self.canWin(nextState):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.canWin("++++"))
