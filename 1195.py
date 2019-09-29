from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n + 1
        self.f, self.b, self.fb, self.num = [Lock() for i in 'zzzz']
        self.f.acquire()
        self.b.acquire()
        self.fb.acquire()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(3, self.n, 3):
            if i % 5:
                self.f.acquire()
                printFizz()
                self.num.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(5, self.n, 5):
            if i % 3:
                self.b.acquire()
                printBuzz()
                self.num.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(15, self.n, 15):
            self.fb.acquire()
            printFizzBuzz()
            self.num.release()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n):
            self.num.acquire()
            if i % 15 == 0:
                self.fb.release()
            elif i % 3 == 0:
                self.f.release()
            elif i % 5 == 0:
                self.b.release()
            else:
                printNumber(i)
                self.num.release()
