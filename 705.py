class MyHashSet:

    def __init__(self):
        self.set = 0

    def add(self, key: int) -> None:
        self.set |= 1 << key

    def remove(self, key: int) -> None:
        self.set &= ~(1 << key)

    def contains(self, key: int) -> bool:
        return self.set & 1 << key
