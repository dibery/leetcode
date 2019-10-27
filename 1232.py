class Solution:
    def checkStraightLine(self, pt: List[List[int]]) -> bool:
        dx, dy = pt[0][0] - pt[1][0], pt[0][1] - pt[1][1]
        for i in range(len(pt)):
            for j in range(i, len(pt)):
                DX, DY = pt[i][0] - pt[j][0], pt[i][1] - pt[j][1]
                if DX * dy != DY * dx:
                    return False
        return True
