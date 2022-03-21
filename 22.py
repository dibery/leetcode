class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def find(ans, left, right, now):
            if left == right == 0:
                ans.append(now)
                return
            if left:
                find(ans, left - 1, right, now + '(')
            if right > left:
                find(ans, left, right - 1, now + ')')
        
        find(ans, n, n, '')
        return ans
