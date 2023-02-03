class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        s, g = [], []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s.append(secret[i])
                g.append(guess[i])
        for i in range(len(s)):
            if s[i] in g:
                cows += 1
                g.remove(s[i])
        return f"{bulls}A{cows}B"


if __name__ == '__main__':
    s = Solution()
    print(s.getHint("1807", "7810"))
    print(s.getHint("1123", "0111"))
    print(s.getHint("1", "0"))
    print(s.getHint("1", "1"))
