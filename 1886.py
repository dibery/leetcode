from numpy import array, rot90
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        mat = array(mat)
        target = array(target)
        for i in range(4):
            target = rot90(target)
            if (target == mat).all():
                return True
        return False
