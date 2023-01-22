from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curr = []
        num_of_letters = 0
        for word in words:
            if num_of_letters + len(word) + len(curr) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    curr[i % (len(curr) - 1 or 1)] += ' '
                res.append(''.join(curr))
                curr, num_of_letters = [], 0
            curr += [word]
            num_of_letters += len(word)
        return res + [' '.join(curr).ljust(maxWidth)]


if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(Solution().fullJustify(words, maxWidth))
