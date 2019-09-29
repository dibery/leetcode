from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lf, self.lb = [Lock() for i in 'zz']
        self.lb.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lf.acquire()
            printFoo()
            self.lb.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lb.acquire()
            printBar()
            self.lf.release()
