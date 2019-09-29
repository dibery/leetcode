class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        have, use = [text.count(i) for i in 'ablon'], ['balloon'.count(i) for i in 'ablon']
        return min([have[i] // use[i] for i in range(5)])
