from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        return map(''.join, product(*(key[int(d)] for d in digits))) if digits else []
