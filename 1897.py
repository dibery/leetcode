from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = Counter(''.join(words))
        return all(i % len(words) == 0 for i in c.values())
