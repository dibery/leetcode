class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        seq = []
        def pre(node):
            if not node:
                return
            if high >= node.val >= low:
                seq.append(node.val)
            pre(node.left)
            pre(node.right)
        pre(root)
        if not seq:
            return
        root = TreeNode(seq[0])
        def ins(root, val):
            if val < root.val:
                if root.left:
                    ins(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    ins(root.right, val)
                else:
                    root.right = TreeNode(val)
        for i in seq[1:]:
            ins(root, i)
        return root
