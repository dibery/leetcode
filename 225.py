from queue import Queue
class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        for i in range(self.q.qsize() - 1):
            self.q.put(self.q.get())
        return self.q.get()

    def top(self) -> int:
        return self.q.queue[-1]

    def empty(self) -> bool:
        return self.q.empty()
