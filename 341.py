class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.it = self.traverse(nestedList)
    
    def traverse(self, nl):
        if type(nl) == list:
            for i in nl:
                yield from self.traverse(i)
        if nl.getInteger() is not None:
            yield nl.getInteger()
        else:
            for i in nl.getList():
                yield from self.traverse(i)
    
    def next(self) -> int:
        return self.nv
    
    def hasNext(self) -> bool:
        try:
            self.nv = next(self.it)
            return True
        except:
            return False
