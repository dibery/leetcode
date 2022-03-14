class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correct = {'}': '{', ']': '[', ')': '('}
        for c in s:
            if c in '([{':
                stack.append(c)
            elif stack and stack[-1] == correct[c]:
                stack.pop()
            else:
                return False
        return not stack
