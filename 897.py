class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.root = self.ins = None
        def add(val):
            if not self.root:
                self.root = self.ins = TreeNode(val)
            else:
                self.ins.right = TreeNode(val)
                self.ins = self.ins.right
        def dfs(node):
            if node:
                dfs(node.left)
                add(node.val)
                dfs(node.right)
        dfs(root)
        return self.root
