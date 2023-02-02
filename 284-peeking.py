# Below is the interface for Iterator, which is already defined for you.

class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.index = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.index < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        result = self.nums[self.index]
        self.index += 1
        return result


class PeekingIterator:
    # Your PeekingIterator object will be instantiated and called as such:
    # iter = PeekingIterator(Iterator(nums))
    # while iter.hasNext():
    #     val = iter.peek()   # Get the next element but not advance the iterator.
    #     iter.next()         # Should return the same value as [val].
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked is None:
            self.peeked = self.iterator.next()
        return self.peeked

    def next(self):
        """
        :rtype: int
        """
        if self.peeked is not None:
            result = self.peeked
            self.peeked = None
        else:
            result = self.iterator.next()
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeked is not None or self.iterator.hasNext()


if __name__ == "__main__":
    nums = [1, 2, 3]
    iter = PeekingIterator(Iterator(nums))
    while iter.hasNext():
        val = iter.peek()   # Get the next element but not advance the iterator.
        print(val)
        iter.next()         # Should return the same value as [val].
