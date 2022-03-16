class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        for p in popped:
            while pushed and (not stk or stk[-1] != p):
                stk.append(pushed.pop(0))
            if not stk or stk[-1] != p:
                return False
            stk.pop()
        return True
