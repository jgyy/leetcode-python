from typing import List


class ZigzagIterator:
    # Your ZigzagIterator object will be instantiated and called as such:
    # i, v = ZigzagIterator(v1, v2), []
    # while i.hasNext(): v.append(i.next())
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.index = [0, 0]
        self.current = 0

    def next(self) -> int:
        result = self.vectors[self.current][self.index[self.current]]
        self.index[self.current] += 1
        self.current = (self.current + 1) % len(self.vectors)
        return result

    def hasNext(self) -> bool:
        while self.index[self.current] == len(self.vectors[self.current]):
            self.current = (self.current + 1) % len(self.vectors)
            if self.index[self.current] == len(self.vectors[self.current]):
                return False
        return True


if __name__ == '__main__':
    i, v = ZigzagIterator([1, 2], [3, 4, 5, 6]), []
    while i.hasNext():
        v.append(i.next())
    print(v)
    assert v == [1, 3, 2, 4, 5, 6]
    i, v = ZigzagIterator([1, 1], [1, 1, 1, 1]), []
    while i.hasNext():
        v.append(i.next())
    print(v)
    assert v == [1, 1, 1, 1, 1, 1]
    i, v = ZigzagIterator([1, 2, 3], [4, 5, 6, 7, 8]), []
    while i.hasNext():
        v.append(i.next())
    print(v)
    assert v == [1, 4, 2, 5, 3, 6, 7, 8]
