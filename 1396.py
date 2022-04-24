class UndergroundSystem:

    def __init__(self):
        self.entry = {}
        self.record = {}

    def checkIn(self, id: int, s: str, t: int) -> None:
        self.entry[id] = (s, t)

    def checkOut(self, id: int, s: str, t: int) -> None:
        self.record.setdefault((self.entry[id][0], s), []).append(t - self.entry[id][1])

    def getAverageTime(self, s: str, t: str) -> float:
        return sum(self.record[s, t]) / len(self.record[s, t])
