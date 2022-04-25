class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.val = None

    def peek(self):
        if self.val is None:
            self.val = self.iter.next()
        return self.val

    def next(self):
        t = self.peek()
        self.val = None
        return t

    def hasNext(self):
        return self.val is not None or self.iter.hasNext()
