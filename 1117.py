from threading import Lock

class H2O:
    def __init__(self):
        self.H = self.O = None
        self.h = self.o = 0
        self.L = Lock()
    
    def output(self):
        if self.h >= 2 and self.o >= 1:
            self.h, self.o = self.h - 2, self.o - 1
            (self.H(), self.H(), self.O())
        self.L.release()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.L.acquire()
        self.H = releaseHydrogen
        self.h += 1
        self.output()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.L.acquire()
        self.O = releaseOxygen
        self.o += 1
        self.output()
