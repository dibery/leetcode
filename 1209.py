import re
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        pattern = '(.)' + '\\1' * (k - 1)
        while re.search(pattern, s):
            s = re.sub(pattern, '', s)
        return s
