class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.x = self.y = self.last = None
        def dfs(node):
            if node:
                dfs(node.left)
                if self.last and self.last.val > node.val:
                    if not self.x:
                        self.x = self.last
                    self.y = node
                self.last = node
                dfs(node.right)
        dfs(root)
        self.x.val, self.y.val = self.y.val, self.x.val
