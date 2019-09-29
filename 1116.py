from threading import Lock
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lz, self.le, self.lo = [Lock() for i in 'zzz']
        self.le.acquire()
        self.lo.acquire()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.lz.acquire()
            printNumber(0)
            if i % 2:
                self.le.release()
            else:
                self.lo.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.le.acquire()
            printNumber(i)
            self.lz.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.lo.acquire()
            printNumber(i)
            self.lz.release()
