from typing import List
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


def read4(buf4: List[str]) -> int:
    return len(buf4)


class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf4 = [''] * 4
        cnt = 0
        while cnt < n:
            r = read4(buf4)
            if not r:
                break
            for i in range(r):
                if cnt == n:
                    break
                buf[cnt] = buf4[i]
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().read([*"abc"], 4))
    print(Solution().read([*"abcde"], 5))
    print(Solution().read([*"abcdABCD1234"], 12))
