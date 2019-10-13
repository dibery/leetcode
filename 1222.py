class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        for i in range(king[0] - 1, -1, -1):
            if [i, king[1]] in queens:
                ans.append([i, king[1]])
                print([i, king[1]])
                break
        for i in range(king[0] + 1, 8):
            if [i, king[1]] in queens:
                ans.append([i, king[1]])
                print([i, king[1]])
                break
        for i in range(king[1] - 1, -1, -1):
            if [king[0], i] in queens:
                ans.append([king[0], i])
                print([king[0], i])
                break
        for i in range(king[1] + 1, 8):
            if [king[0], i] in queens:
                ans.append([king[0], i])
                print([king[0], i])
                break
        for i in range(1, 8):
            if max(king) + i >= 8:
                break
            if [king[0] + i, king[1] + i] in queens:
                ans.append([king[0] + i, king[1] + i])
                break
        for i in range(1, 8):
            if min(king) - i < 0:
                break
            if [king[0] - i, king[1] - i] in queens:
                ans.append([king[0] - i, king[1] - i])
                break
        for i in range(8):
            if king[0] + i >= 8 or king[1] - i < 0:
                break
            if [king[0] + i, king[1] - i] in queens:
                ans.append([king[0] + i, king[1] - i])
                break
        for i in range(8):
            if king[1] + i >= 8 or king[0] - i < 0:
                break
            if [king[0] - i, king[1] + i] in queens:
                ans.append([king[0] - i, king[1] + i])
                break
        return ans
