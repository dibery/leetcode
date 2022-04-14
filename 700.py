class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and val != root.val:
            root = root.left if val < root.val else root.right
        return root
