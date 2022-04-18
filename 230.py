class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = self.ans = 0
        def dfs(node):
            if node and self.count < k:
                dfs(node.left)
                self.count += 1
                if self.count == k:
                    self.ans = node.val
                dfs(node.right)
        dfs(root)
        return self.ans
