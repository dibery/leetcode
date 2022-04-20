class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.traverse = self.dfs(root)
        self.val = next(self.traverse)

    def next(self) -> int:
        v = self.val
        try:
            self.val = next(self.traverse)
        except:
            self.val = None
        return v

    def hasNext(self) -> bool:
        return self.val is not None
        
    def dfs(self, node):
        if node:
            yield from self.dfs(node.left)
            yield node.val
            yield from self.dfs(node.right)
