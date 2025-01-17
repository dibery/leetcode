class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        val = 1
        for i in derived:
            val ^= i
        return bool(val)
