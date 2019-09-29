from collections import Counter
from itertools import compress
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        words = Counter([''.join(sorted(set(w))) for w in words if len(set(w)) < 8])
        return [(sum(words[''.join(sorted(compress(p, map(int, bin(i)[2:].zfill(7)))))] for i in range(64, 128))) for p in puzzles]