class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.s = 0
        def dfs(node):
            if node:
                dfs(node.right)
                self.s = node.val = node.val + self.s
                dfs(node.left)
        dfs(root)
        return root
