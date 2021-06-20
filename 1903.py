[2~import re
class Solution:
    def largestOddNumber(self, num: str) -> str:
        return re.sub('[02468]*$', '', num)
