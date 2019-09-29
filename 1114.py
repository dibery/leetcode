import threading

class Foo:
    def __init__(self):
        self.L1, self.L2, self.L3 = [threading.Lock() for i in 'zzz']
        self.L2.acquire()
        self.L3.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.L2.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.L2.acquire()
        printSecond()
        self.L3.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.L3.acquire()
        printThird()
