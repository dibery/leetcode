class Solution:
    def test(self, head, root) -> bool:
        if head == None:
            return True
        if root == None or head.val != root.val:
            return False
        return self.test(head.next, root.left) or self.test(head.next, root.right)
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        return self.test(head, root) or root.left and self.isSubPath(head, root.left) or root.right and self.isSubPath(head, root.right)